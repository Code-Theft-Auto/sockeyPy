import discord
from discord.ext import menus, commands
import datetime


class DefaultPageSource(menus.ListPageSource):
    def __init__(self, title, data):
        self.title = title
        super().__init__(data, per_page=10)

    async def format_page(self, menu, entries):
        embed = discord.Embed(color=menu.ctx.bot.embed_color, title=self.title, timestamp=datetime.datetime.utcnow())
        for entry in entries:
            embed.add_field(name=entry[0], value=entry[1], inline=False)
        embed.set_footer(text=f'Page {menu.current_page + 1}/{self.get_max_pages()}')
        return embed


class SecondPageSource(menus.ListPageSource):
    def __init__(self, title, data):
        self.title = title
        super().__init__(data, per_page=10)

    async def format_page(self, menu, entries):
        embed = discord.Embed(title=self.title, color=menu.ctx.bot.embed_color, timestamp=datetime.datetime.utcnow())
        embed.description = "\n".join([f"{name}: {value}" for name, value in entries])
        embed.set_footer(text=f'Page {menu.current_page + 1}/{self.get_max_pages()}')
        return embed


class MenuPages(discord.ui.View):
    """View Paginator for ext.menus"""
    def __init__(self, source: menus.PageSource, ctx: commands.Context, *, compact: bool = False):
        super().__init__(timeout=120.0)
        self._source = source
        self.current_page = 0
        self.ctx = ctx
        self.message = None
        self.compact = compact
        self.clear_items()
        self.fill_items()

    def fill_items(self) -> None:
        if self._source.is_paginating():
            use_last_and_first = self._source.get_max_pages() is not None and self._source.get_max_pages() >= 2
            if use_last_and_first:
                self.add_item(self.first_page)

            self.add_item(self.before_page)
            self.add_item(self.next_page)

            if use_last_and_first:
                self.add_item(self.last_page)

            self.add_item(self.stop_page)

    def update_labels(self, page_number):
        self.first_page.disabled = page_number == 0
        max_pages = self._source.get_max_pages()

        self.last_page.disabled = (
                max_pages is None or (page_number + 1) >= max_pages
        )
        self.next_page.disabled = (
                max_pages is not None and (page_number + 1) >= max_pages
        )
        self.before_page.disabled = page_number == 0

        if max_pages is not None:
            self.last_page.disabled = (page_number + 1) >= max_pages
            if (page_number + 1) >= max_pages:
                self.next_page.disabled = True
            if page_number == 0:
                self.before_page.disabled = True

    async def _get_kwargs_from_page(self, page):
        value = await discord.utils.maybe_coroutine(self._source.format_page, self, page)
        if isinstance(value, dict):
            return value
        elif isinstance(value, str):
            return {'content': value, 'embed': None}
        elif isinstance(value, discord.Embed):
            return {'embed': value, 'content': None}

    async def show_page(self, interaction, page_number):
        page = await self._source.get_page(page_number)
        self.current_page = page_number
        kwargs = await self._get_kwargs_from_page(page)
        self.update_labels(page_number)
        if kwargs:
            if interaction.response.is_done():
                await self.message.edit(**kwargs, view=self)
            else:
                await interaction.response.edit_message(**kwargs, view=self)

    async def show_checked_page(self, interaction, page_number):
        max_pages = self._source.get_max_pages()
        try:
            if max_pages is None:
                await self.show_page(interaction, page_number)
            elif max_pages > page_number >= 0:
                await self.show_page(interaction, page_number)
        except IndexError:
            pass

    async def start(self) -> None:
        await self._source._prepare_once()
        page = await self._source.get_page(0)
        kwargs = await self._get_kwargs_from_page(page)
        self.update_labels(0)
        self.message = await self.ctx.send(**kwargs, view=self)

    async def on_timeout(self) -> None:
        await self.message.edit(view=None)

    async def on_error(self, interaction, error, item) -> None:
        await interaction.response.send_message(f"**Error:** {error}", ephemeral=True)

    async def interaction_check(self, interaction) -> bool:
        if interaction.user == self.ctx.author:
            return True
        await interaction.response.send_message("you cant use these buttons \:( ", ephemeral=True)
        return False

    @discord.ui.button(emoji='⏪', style=discord.ButtonStyle.grey)
    async def first_page(self, interaction, button):
        await self.show_page(interaction, 0)

    @discord.ui.button(emoji='◀️', style=discord.ButtonStyle.grey)
    async def before_page(self, interaction, button):
        await self.show_checked_page(interaction, self.current_page - 1)

    @discord.ui.button(emoji='▶️', style=discord.ButtonStyle.grey)
    async def next_page(self, interaction, button):
        await self.show_checked_page(interaction, self.current_page + 1)

    @discord.ui.button(emoji='⏩', style=discord.ButtonStyle.grey)
    async def last_page(self, interaction, button):
        await self.show_page(interaction, self._source.get_max_pages() - 1)

    @discord.ui.button(emoji='🗑', style=discord.ButtonStyle.red)
    async def stop_page(self, interaction, button):
        await self.message.edit(view=None)
        self.stop()