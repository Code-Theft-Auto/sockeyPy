import discord
from discord.ext import commands, menus
from utils.menuUtils import MenuPages
from utils.help import CustomHelp
import datetime
import io


class ServerPageSource(menus.ListPageSource):
    def __init__(self, data):
        super().__init__(data, per_page=10)

    async def format_page(self, menu, entries):
        embed = discord.Embed(title="Servers")
        for entry in entries:
            embed.add_field(name=entry[0], value=entry[1], inline=False)
        embed.set_footer(text=f'Page {menu.current_page + 1}/{self.get_max_pages()}')
        return embed


class Info(commands.Cog):
    emoji = "📋"

    def __init__(self, bot):
        self.bot = bot
        bot.help_command = CustomHelp()
        bot.help_command.cog = self


async def setup(bot):
    await bot.add_cog(Info(bot))