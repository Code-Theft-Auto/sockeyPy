import discord
from discord.ext.commands import Cog,Bot
from discord.ext.commands.context import Context
import sys
sys.path.insert(1, '../modules')
from config import nemoji

class ServerOnly(Cog):
    '''my server only'''
    
    __slots__ = ('bot')

    def __init__(self, bot):
        self.bot = bot

    @Cog.listener()
    async def on_message(self,ctx:Context):
        if ctx.channel.id == 943503892656816198:
            emoji = []
            for _ in ctx.message.lower():
                if _.isdecimal():
                    emoji.append(f':{nemoji.get(_)}:')

                elif _.isalpha():
                    emoji.append(f':regional_indicator_{_}:')
        
                else:
                    emoji.append(_)
            await ctx.send(''.join(emoji))
            await self.bot.process_commands(ctx.message)
        else:
            pass
        
    
def setup(bot:Bot):
    bot.add_cog(ServerOnly(bot))  
