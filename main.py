import os
import sys
sys.path.insert(1, './modules')

import discord
import asyncio
from discord.ext import commands
import aiohttp

beats_activity = [discord.ActivityType.listening, "Beats"]
bot = commands.Bot(command_prefix='.',intents=discord.Intents.all(), activity=discord.Activity(type=beats_activity[0], name=beats_activity[1]),status=discord.Status.dnd)

cogs = [
    'general',
    'music',
    'coglur',
    'help'
]


@bot.event
async def on_ready():
    print("logged in as {0.user}".format(bot))

async def load_extension():
    for file in cogs:
        await bot.load_extension(f'cogs.{file}')

async def main():
    async with bot:
        await load_extension()
        TOKEN = str(os.getenv('TOKEN'))
        await bot.start(TOKEN)

asyncio.run(main())
