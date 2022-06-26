import sys
import discord
import asyncio
import base64 as b64
sys.path.insert(1, '../modules')

from googlesearch import search
import impfunctions as func
from discord.ext import commands


ctx = discord.ext.commands.context.Context
message = discord.ext.commands.context.Context
DOGAPI = "http://thedogapi.com/api/images/get.php"
CATAPI = "http://thecatapi.com/api/images/get.php"


class General(commands.Cog):
    emoji="🔖"
    def __init__(self, bot):
        self.bot = bot


    @commands.command(name="ping")
    async def ping_(self, ctx):
        """show the ping of the bot from the user """
        async with ctx.typing():
            await asyncio.sleep(0.2)
        await ctx.send(f"pong {round(self.bot.latency*1000)} ms")

    @commands.command(name="dice")
    async def dice_(self, ctx):
        """ it rolls dice and sends the random number from 1 to 6"""
        async with ctx.typing():
            await asyncio.sleep(0.2)
        rand_num = func.roll_dice()
        await ctx.send(rand_num)

    @commands.command(name="cat")
    async def cat_(self, ctx):
        """sends a cute picture of a cat"""
        await ctx.send(await func.getCatPicture())

    @commands.command(name="dog")
    #dog pic command
    async def dog_(self, ctx):
        """sends a cure picture of a dog"""
        await ctx.send(await func.getDogPicture())


    @commands.command(name="rnum")
    async def rnum_(self,ctx,a: int,b: int,):
        """sends a random number between the given numbers"""
        await ctx.send(func.randnum(a=a, b=b))


    @commands.command(description="encodes a string to base64 `.encode <string>`")
    async def encode(self, ctx, text:str):
        """encodes a string to base64"""
        await ctx.message.delete()
        text = text.encode()
        text64 = str(b64.b64encode(text))
        await ctx.author.send(f"encoded string: {text64}")

    @commands.command(description="decodes encoded string back to how it used to be `.decode <encoded string>`")
    async def decode(self, ctx, message_toencode):
        """decodes encoded string back to how it used to be"""
        await ctx.message.delete()
        text = text.encode()
        text64 = str(b64.b64decode(text))
        await ctx.author.send(f"decoded string: {text64}")


    @commands.command(name="meme",description="sends some nice memes `.meme`")
    async def meme_(self,ctx):
        """sends some nice memes """

        em = await func.meme()
        await ctx.send(embed=em,)



    @commands.command(name="gs")
    async def gs(self, ctx, *, query):
        """#googleit"""
        await ctx.author.send(f"Here are the links related to your question!")
        for j in search(query, safe='on', start=1, stop=1):
            await ctx.author.send(f"\n:point_right: {j}")
            await ctx.author.send("Have any more questions:question:\nFeel free to ask again :smiley: !")

    @commands.command(name="servers")
    async def servers_(self,ctx):
        """shows the number servers the bot is in"""
        names = []
        for guild in self.bot.guilds:names.append(f"**`{guild.name}`**")
        await ctx.send(f"**guilds: {len(self.bot.guilds)}**",embed=discord.Embed(description=f"\n".join(names),color=discord.Color.green()))


async def setup(bot):
    await bot.add_cog(General(bot))
