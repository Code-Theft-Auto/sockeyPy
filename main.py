import os
import sys
sys.path.insert(1, './modules')

import discord,asyncio
import keep_alive
from googlesearch import search
from discord.ext import commands
#from discord_slash import SlashCommand



bot = commands.Bot(command_prefix='.',help_command=None,intents=discord.Intents.all())
#slash = SlashCommand(bot,
                    # sync_commands=True,
                     #sync_on_cog_reload=True,
                     #application_id=916685474364534805)
beats_activity = [discord.ActivityType.listening, "Beats"]

cogs = [
    'general',
    'music',
    'coglur',
    'help'
]


@bot.event
async def on_ready():
    print("logged in as {0.user}".format(bot))
    await bot.change_presence(activity=discord.Activity(
        type=beats_activity[0], name=beats_activity[1]),
                              status=discord.Status.dnd)
async def load_extension():
    for file in cogs:
        await bot.load_extension(f'cogs.{file}')

async def main():
    async with bot:
        await load_extension()
        TOKEN = str(os.getenv('TOKEN')) or input('enter token: ')
        await bot.start(TOKEN)


# keep_alive.keep_alive()
#bot.run(TOKEN) #client login
asyncio.run(main())