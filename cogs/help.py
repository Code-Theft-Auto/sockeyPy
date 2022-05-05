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


    @commands.command(help="Show bot uptime")
    async def uptime(self, ctx):
        await ctx.send(f"<t:{int(datetime.datetime.timestamp(self.bot.uptime))}:R>")


    @commands.command(help="See list of servers")
    @commands.is_owner()
    async def guildlist(self, ctx):
        data = []
        for guild in self.bot.guilds:
            to_append = (f"{guild.name}", f"**Owner** {guild.owner} **Member** {guild.member_count} **ID** {guild.id}")
            data.append(to_append)
        menu = MenuPages(ServerPageSource(data), ctx)
        await menu.start()

async def setup(bot):
    await bot.add_cog(Info(bot))