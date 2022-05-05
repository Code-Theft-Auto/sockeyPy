import discord
from discord.ext import commands
from discord_slash.model import ButtonStyle
from discord_slash.utils.manage_components import ComponentContext, wait_for_component,create_button,create_actionrow


NEXTBUTTON = [create_button(ButtonStyle.blurple, label="->", custom_id="NextPage")]
BEFOREBUTTON = [create_button(ButtonStyle.blurple,label="<-",custom_id="BeforePage")]
AboutPage = discord.Embed(
    title="Help",
    color=discord.Color.blurple,
    ).add_field(
            name="General",
            value="most of the general commands are here including image command and other stuff",
            inline=True
            ).add_field(
                name="Music",
                value="all the music commands are here",
                inline=True
            )

class Help(commands.Cog):
    """Sends this help message"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx,):
        pass
        
        
        


def setup(bot):
    bot.add_cog(Help(bot))