import os
import sys
sys.path.insert(1, './modules')

import discord
import keep_alive
from googlesearch import search
from discord.ext import commands
from discord_slash import SlashCommand



bot = commands.Bot(command_prefix='.', help_command=None)

slash = SlashCommand(bot,
                     sync_commands=True,
                     sync_on_cog_reload=True,
                     application_id=916685474364534805)

beats_activity = [discord.ActivityType.listening, "Beats"]

extensions = ["music", "general"]
bot.load_extension("music")
bot.load_extension("general")
bot.load_extension("slashcog")



@bot.event
#on ready
async def on_ready():
    print("logged in as {0.user}".format(bot))
    await bot.change_presence(activity=discord.Activity(
        type=beats_activity[0], name=beats_activity[1]),
                              status=discord.Status.dnd)





@bot.command()
async def gs(ctx,*, query):
    await ctx.author.send(f"Here are the links related to your question!")
    for j in search(query, safe='on', start=1, stop=1):
        await ctx.author.send(f"\n:point_right: {j}")
        await ctx.author.send("Have any more questions:question:\nFeel free to ask again :smiley: !")


@bot.command()
async def servers(ctx):
    await ctx.send(
        embed=discord.Embed(description=f"`i am in {len(bot.guilds)} guilds`",
                            color=discord.Color.green()))


@bot.command()
async def rawserv(ctx):
    await ctx.send(bot.guilds)

@bot.command()
async def servname(ctx):
    names = []
    for guild in bot.guilds:names.append(f"**`{guild.name}`**")
    await ctx.send(embed=discord.Embed(description=f"\n".join(names),color=discord.Color.green()))





TOKEN = str(os.getenv('TOKEN'))
keep_alive.keep_alive()
bot.run(TOKEN)  # client login
