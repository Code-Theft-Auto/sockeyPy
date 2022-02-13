import os,sys,discord,asyncio
import base64 as b64
sys.path.insert(1, '../modules')

import possiblekeywords
from googlesearch import search
import impfunctions as func
from discord.ext.commands import Bot
from discord.ext import commands
from discord_slash.model import ButtonStyle
from discord_slash.utils.manage_components import ComponentContext, wait_for_component,create_button,create_actionrow


NEXTBUTTON = [create_button(ButtonStyle.green, label="Next", custom_id="NextMeme")]
ctx = discord.ext.commands.context.Context
message = discord.ext.commands.context.Context



DOGAPI = "http://thedogapi.com/api/images/get.php"
CATAPI = "http://thecatapi.com/api/images/get.php"


class General(commands.Cog):
    '''general commands'''
    
    __slots__ = ('bot')

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ping")  #ping pong command
    async def ping_(self, ctx):
        async with ctx.typing():
            await asyncio.sleep(0.2)
        await ctx.send(f"pong {round(self.bot.latency*1000)} ms")

    @commands.command(name="dice")
    #roll dice command
    async def dice_(self, ctx):
        async with ctx.typing():
            await asyncio.sleep(0.2)
        rand_num = func.roll_dice()
        await ctx.send(rand_num)

    @commands.command(name="cat")
    #cat pic command
    async def cat_(self, ctx):
        await ctx.send(func.getCatPicture())

    @commands.command(name="dog")
    #dog pic command
    async def dog_(self, ctx):
        await ctx.send(func.getDogPicture())
    
    @commands.command(name="math")
    #math operations command
    async def math_(self, ctx, arg: str):
        await ctx.send(func.math_eval(arg))

    @commands.command(name="rnum")
    async def rnum_(self,ctx,a: int,b: int,):
        await ctx.send(func.randnum(a=a, b=b))

    @commands.command(help_command=True, name="help")
    async def help_(self, ctx):
        async with ctx.typing():
            await asyncio.sleep(3)
        # help command
        embed = func.help()
        await ctx.send(content="**SOCKEY HELP**", embed=embed)

    @commands.command()
    async def encode(self, ctx, message_toencode):
        await ctx.message.delete()

        message_toencode = str(message_toencode).encode()

        message_toencode = b64.b64encode(message_toencode)
        message_toencode = str(message_toencode)
        message_toencode = message_toencode.replace("b'", "")
        message_toencode = message_toencode.replace("'", "")
        
        await ctx.author.send(f"encoded string: {message_toencode}")

    @commands.command()
    async def decode(self, ctx, message_toencode):
        await ctx.message.delete()

        message_toencode = str(message_toencode).encode()

        message_toencode = b64.b64decode(message_toencode)
        message_toencode = str(message_toencode)
        message_toencode = message_toencode.replace("b'", "")
        message_toencode = message_toencode.replace("'", "")

        await ctx.author.send(f"decoded string: {message_toencode}")

    @commands.command()
    async def encrypt(self, ctx, string: str):
        await ctx.message.delete()
        token, key = func.encrypt(string)
        await ctx.author.send(f"encrypted string: {token} | key: {key}")

    @commands.command()
    async def decrypt(self, ctx, token, key):
        decodedstr = func.decrypt(token, key)
        await ctx.author.send(f"decrypted string: {decodedstr}")
    
    @commands.command(name="meme")
    async def meme_(self,ctx):
        em = func.meme()
        await ctx.send(embed=em, components=[create_actionrow(*NEXTBUTTON)])

        while 1:
            try:
                button_ctx: ComponentContext = await wait_for_component(
                self.bot, components=NEXTBUTTON, timeout=10)

                await button_ctx.edit_origin(embed=func.meme())
            except asyncio.exceptions.TimeoutError:
                break
    
    @commands.command(name="gs")
    async def gs(self, ctx, *, query):
        await ctx.author.send(f"Here are the links related to your question!")
        for j in search(query, safe='on', start=1, stop=1):
            await ctx.author.send(f"\n:point_right: {j}")
            await ctx.author.send("Have any more questions:question:\nFeel free to ask again :smiley: !")
    
    @commands.command(name="servers")
    async def servers(self, ctx):
        await ctx.send(
            embed=discord.Embed(description=f"`i am in {len(self.bot.guilds)} guilds`",
                            color=discord.Color.green()))

    @commands.command(name="servname")
    async def servname(self,ctx):
        names = []
        for guild in self.bot.guilds:names.append(f"**`{guild.name}`**")
        await ctx.send(embed=discord.Embed(description=f"\n".join(names),color=discord.Color.green()))


def setup(bot):
    bot.add_cog(General(bot))
