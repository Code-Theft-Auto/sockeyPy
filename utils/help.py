import discord
from discord.ext import commands, menus
from .menuUtils import MenuPages
from typing import Dict, List, Union, Optional, Any
import itertools



class HelpSelectMenu(discord.ui.Select['HelpMenuPage']):
    def __init__(self, command: Dict[commands.Cog, List[commands.Command]], bot):
        super().__init__(
            placeholder='Choose a category...',
            min_values=1,
            max_values=1,
            row=0,
        )
        self.commands = command
        self.bot = bot
        self.__fill_options()

    def __fill_options(self) -> None:
        self.add_option(
            label='Index',
            emoji='🏠',
            value='__index',
            description='The help page showing how to use the bot.',
        )
        for cog, command in self.commands.items():
            if not command:
                continue
            description = cog.description.split('\n', 1)[0] or None
            emoji = getattr(cog, 'emoji', None)
            self.add_option(label=cog.qualified_name, value=cog.qualified_name, description=description, emoji=emoji)

    async def callback(self, interaction: discord.Interaction):
        assert self.view is not None
        value = self.values[0]
        if value == '__index':
            await self.view.rebind(FrontPageSource(), interaction)
        else:
            cog = self.bot.get_cog(value)
            if cog is None:
                await interaction.response.send_message('Somehow this category does not exist?', ephemeral=True)
                return

            command = self.commands[cog]
            if not command:
                await interaction.response.send_message('This category has no commands for you', ephemeral=True)
                return

            source = CogPageSource(cog, command, prefix=self.view.ctx.clean_prefix)
            await self.view.rebind(source, interaction)


class FrontPageSource(menus.PageSource):
    def is_paginating(self) -> bool:
        # This forces the buttons to appear even in the front page
        return True

    def get_max_pages(self) -> Optional[int]:
        # There's only one actual page in the front page
        # However we need at least 2 to show all the buttons
        return 2

    async def get_page(self, page_number: int) -> Any:
        # The front page is a dummy
        self.index = page_number
        return self

    def format_page(self, menu, page):
        embed = discord.Embed(title='Bot Help')
        embed.description = f"""
Use "{menu.ctx.clean_prefix}help command" for more info on a command.
Use "{menu.ctx.clean_prefix}help category" for more info on a category.
Use the dropdown menu below to select a category.
        """

        embed.add_field(
            name='Support Server',
            value='have some problems?? join https://dsc.gg/erfer',
            inline=False,
        )

        if self.index == 0:
            embed.add_field(
                name='Information',
                value=(
                        f"currently running on **{len(menu.ctx.bot.guilds)}** servers and watching **{len(menu.ctx.bot.users)}** users nice\n"
                        
                    ),
                inline=False
            )
        elif self.index == 1:
            entries = (
                ('<argument>', 'This means the argument is __**required**__.'),
                ('[argument]', 'This means the argument is __**optional**__.'),
                ('[A|B]', 'This means that it can be __**either A or B**__.'),
                (
                    '[argument...]',
                    'This means you can have multiple arguments.\n'
                    'Now that you know the basics, it should be noted that...\n'
                    '__**You do not type in the brackets!**__',
                ),
            )

            embed.add_field(name='How do I use this bot?', value='Reading the bot signature is pretty simple.')

            for name, value in entries:
                embed.add_field(name=name, value=value, inline=False)

        return embed


class HelpMenuPage(MenuPages):
    def __init__(self, source: menus.PageSource, ctx: commands.Context):
        super().__init__(source, ctx=ctx)

    def add_categories(self, command: Dict[commands.Cog, List[commands.Command]]) -> None:
        self.clear_items()
        self.add_item(HelpSelectMenu(command, self.ctx.bot))
        self.fill_items()

    async def rebind(self, source: menus.PageSource, interaction: discord.Interaction) -> None:
        self._source = source
        self.current_page = 0

        await self._source._prepare_once()
        page = await self._source.get_page(0)
        kwargs = await self._get_kwargs_from_page(page)
        self.update_labels(0)
        await interaction.response.edit_message(**kwargs, view=self)


class CogPageSource(menus.ListPageSource):
    def __init__(self, cog: Union[commands.Group, commands.Cog], command: List[commands.Command], *, prefix: str):
        super().__init__(entries=command, per_page=6)
        self.cog = cog
        self.prefix = prefix
        self.title = f'{self.cog.qualified_name} Commands'

    async def format_page(self, menu, entries):
        embed = discord.Embed(title=self.title.title(),
                              description=f'Use "{self.prefix}help command" for more info on a command.',)

        for command in entries:
            signature = f'`{self.prefix}{command.qualified_name} {command.signature}`'
            embed.add_field(name=command.name, value=signature + "\n" + command.short_doc or 'No help given for now...',
                            inline=False)

        embed.set_footer(text=f'Page {menu.current_page + 1}/{self.get_max_pages()}')
        return embed


class CustomHelp(commands.HelpCommand):
    def get_command_signature(self, command):
        return f'{self.context.clean_prefix}{command.qualified_name} {command.signature}'

    async def on_help_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("Sorry but that command does not exist.")

    async def send_bot_help(self, mapping):
        await self.context.channel.typing()
        bot = self.context.bot

        def key(command) -> str:
            cogs = command.cog
            return cogs.qualified_name if cogs else '\U0010ffff'

        entries: List[commands.Command] = await self.filter_commands(bot.commands, sort=True, key=key)

        all_commands: Dict[commands.Cog, List[commands.Command]] = {}
        for name, children in itertools.groupby(entries, key=key):
            if name == '\U0010ffff':
                continue

            cog = bot.get_cog(name)
            all_commands[cog] = sorted(children, key=lambda c: c.qualified_name)

        menu = HelpMenuPage(FrontPageSource(), ctx=self.context)
        menu.add_categories(all_commands)
        await menu.start()

    async def send_cog_help(self, cog_):
        await self.context.channel.typing()
        filtered = await self.filter_commands(cog_.get_commands(), sort=True)

        page = MenuPages(CogPageSource(cog_, filtered, prefix=self.context.clean_prefix), self.context)
        await page.start()

    async def send_group_help(self, group):
        await self.context.channel.typing()
        filtered = await self.filter_commands(group.commands, sort=True)

        page = MenuPages(CogPageSource(group, filtered, prefix=self.context.clean_prefix), self.context)
        await page.start()

    async def send_command_help(self, command):
        await self.context.channel.typing()
        embed = discord.Embed(title=command.name,
                              description=f'Use {self.context.clean_prefix}help [something] for more info on a command or category. \nExample: {self.context.clean_prefix}help Economy')
        if command.help:
            embed.add_field(name="Description", value=f"```{command.help}```", inline=False)
        if command.aliases:
            embed.add_field(name="Aliases", value=f"```{command.aliases}```", inline=False)
        embed.add_field(name="Usage", value=f"```{self.get_command_signature(command)}```", inline=False)
        await self.get_destination().send(embed=embed)