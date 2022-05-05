import discord,Paginator
from discord.ext import commands

AboutPage = discord.Embed(
    title="Help",
    color=discord.Color.blurple(),
    ).add_field(
            name="General",
            value="most of the general commands are here including image command and other stuff",
            inline=True
            ).add_field(
                name="Music",
                value="all the music commands are here",
                inline=True
            )

GeneralPage = discord.Embed(
    title="All General Commands",
    color=discord.Color.blurple(),
).add_field(
    name="ping",
    value="shows the ping of the bot from the user `.ping`",
    inline=True
).add_field(
    name="cat",
    value="sends a cute picture of a cat `.cat`",
    inline=True
).add_field(
    name="dog",
    value="sends a cute picture of a dog `.dog`",
    inline=True
).add_field(
    name="dice",
    value="it rolls dice and sends the random number from 1 to 6 `.dice`",
    inline=True
).add_field(
    name="rnum",
    value="sends a random number between the given numbers `.rnum <min> <max>`",
    inline=True
).add_field(
    name="encode",
    value="encodes a string to base64 `.encode <string>`",
    inline=True
).add_field(
    name="decode",
    value="decodes encoded string back to how it used to be `.decode <encoded string>`",
    inline=True
).add_field(
    name="meme",
    value="sends some nice memes `.meme`",
    inline=True
).add_field(
    name="gs",
    value=" #googleit `.gs <query>`",
    inline=True
).add_field(
    name="servers",
    value="shows the number servers the bot is in `.servers`",
    inline=True
)

AllHelpEmbeds=[AboutPage,GeneralPage]

class Help(commands.Cog):
    """Sends this help message"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx,):
        await Paginator.Simple().start(ctx,AllHelpEmbeds)
        
        


async def setup(bot):
   await bot.add_cog(Help(bot))