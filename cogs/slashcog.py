import os  #imports
import sys
import base64 as b64

sys.path.insert(1, '../modules')

import time
import math
import discord
import modules.keep_alive as keep_alive

import asyncio
#import youtube_dl
import possiblekeywords
from googlesearch import search
import impfunctions as func
from discord.ext import commands
from discord_slash import cog_ext, SlashContext

import random
import itertools
import sys
import traceback

sys.path.insert(1,'./modules')

import json
import impfunctions as func

from async_timeout import timeout
from functools import partial

import youtube_dl
from youtube_dl import YoutubeDL
import youtube_search as yt


ctx = discord.ext.commands.context.Context
message = discord.ext.commands.context.Context

DOGAPI = os.getenv('DOGAPI')
CATAPI = os.getenv('CATAPI')








class General(commands.Cog):
    '''general commands'''
    __slots__ = ('bot')

    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(name="ping",description="ping pong!")  #ping pong command
    async def ping_(self, ctx:SlashContext):
        await ctx.defer()
        
        await ctx.send(f"pong {round(self.bot.latency*1000)} ms")

    @cog_ext.cog_slash(name="dice",description="rolls dice",)
    #roll dice command
    async def dice_(self, ctx:SlashContext):
        await ctx.defer()
        await asyncio.sleep(0.2)
        rand_num = func.roll_dice()
        await ctx.send(rand_num)

    @cog_ext.cog_slash(name="cat",description="sends a picture of cat")
    #cat pic command
    async def cat_(self, ctx:SlashContext):
        await ctx.send(func.getCatPicture())

    @cog_ext.cog_slash(name="dog",description="sends a picture of dog")
    #dog pic command
    async def dog_(self, ctx:SlashContext):
        await ctx.send(func.getDogPicture())



    @cog_ext.cog_slash(name="math",description="do your math!!")
    #math operations command
    async def math_(self, ctx:SlashContext, arg: str):
        await ctx.send(func.math_eval(arg))

    @cog_ext.cog_slash(name="rnum",description="returns a random number")
    async def rnum_(
        self,
        ctx:SlashContext,
        a: int,
        b: int,
    ):
        await ctx.send(func.randnum(a=a, b=b))

    @cog_ext.cog_slash(name="help",description="help??")
    async def help_(self, ctx:SlashContext):
        await ctx.defer()
        
        # help command
        embed = func.help()
        await ctx.send(content="**SOCKEY HELP**", embed=embed)

    @cog_ext.cog_slash(name="encode",description="encodes the given string")
    async def encode(self, ctx:SlashContext,*, message_toencode):
        

        message_toencode = str(message_toencode).encode()

        message_toencode = b64.b64encode(message_toencode)
        message_toencode = str(message_toencode)
        message_toencode = message_toencode.replace("b'", "")
        message_toencode = message_toencode.replace("'", "")

        await ctx.reply(f"encoded string: {message_toencode}",hidden=True)

    @cog_ext.cog_slash(name="decode",description="decodes the given string")
    async def decode(self, ctx:SlashContext, message_toencode):
        

        message_toencode = str(message_toencode).encode()

        message_toencode = b64.b64decode(message_toencode)
        message_toencode = str(message_toencode)
        message_toencode = message_toencode.replace("b'", "")
        message_toencode = message_toencode.replace("'", "")

        await ctx.reply(f"decoded string: {message_toencode}",hidden=True)

    @cog_ext.cog_slash(name="encrypt-extreme",description="this encrypts extremeley dont use big words!!")
    async def encrypt(self, ctx:SlashContext, *,string: str):
        
        token, key = func.encrypt(string)
        await ctx.reply(f"encrypted string: {token} | key: {key}",hidden=True)

    @cog_ext.cog_slash(name="decrypt-extreme",description="decrypts the given token with key")
    async def decrypt(self, ctx:SlashContext, token:str, key:str):
        token = token.encode()
        key = key.encode()
        decodedstr = func.decrypt(token, key)
        await ctx.reply(f"decrypted string: {decodedstr}",hidden=True)





# Suppress noise about console usage from errors
youtube_dl.utils.bug_reports_message = lambda: ''

ytdlopts = {
    'format': 'bestaudio/best',
    'outtmpl': 'downloads/%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0'  
}





lofi_url = [
  "https://www.youtube.com/watch?v=wO_TWt2MWY0",
  "https://www.youtube.com/watch?v=lTRiuFIWV54",
  "https://www.youtube.com/watch?v=eLkWRlPD_hY",
  "https://www.youtube.com/watch?v=wAPCSnAhhC8",
  "https://www.youtube.com/watch?v=BTYAsjAVa3I",
  "https://www.youtube.com/watch?v=_tV5LEBDs7w",
  "https://www.youtube.com/watch?v=zFhfksjf_mY",
  "https://www.youtube.com/watch?v=TURbeWK2wwg",
  "https://www.youtube.com/watch?v=gnZImHvA0ME"

]


ffmpegopts = {
    'before_options': '-nostdin',
    'options': '-vn'
}
ytdl = YoutubeDL(ytdlopts)





class VoiceConnectionError():
    """Custom Exception class for connection errors."""


class InvalidVoiceChannel(VoiceConnectionError):
    """Exception for cases of invalid Voice Channels."""


class YTDLSource(discord.PCMVolumeTransformer):

    def __init__(self, source, *, data, requester):
        super().__init__(source)
        self.requester = requester

        self.title = data.get('title')
        self.web_url = data.get('webpage_url')
        self.duration = data.get('duration')

        # YTDL info dicts (data) have other useful information you might want
        # https://github.com/rg3/youtube-dl/blob/master/README.md

    def __getitem__(self, item: str):
        """Allows us to access attributes similar to a dict.
        This is only useful when you are NOT downloading.
        """
        return self.__getattribute__(item)

    @classmethod
    async def create_source(cls, ctx, search: str, *, loop, download=False):
        loop = loop or asyncio.get_event_loop()

        to_run = partial(ytdl.extract_info, url=search, download=download)
        data = await loop.run_in_executor(None, to_run)

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        embed = discord.Embed(title="", description=f"Queued [{data['title']}]({data['webpage_url']}) [{ctx.author.mention}]", color=discord.Color.green())
        await ctx.send(embed=embed)

        if download:
            source = ytdl.prepare_filename(data)
        else:
            return {'webpage_url': data['webpage_url'], 'requester': ctx.author, 'title': data['title']}

        return cls(discord.FFmpegPCMAudio(source), data=data, requester=ctx.author)

    @classmethod
    async def regather_stream(cls, data, *, loop):
        """Used for preparing a stream, instead of downloading.
        Since Youtube Streaming links expire."""
        loop = loop or asyncio.get_event_loop()
        requester = data['requester']

        to_run = partial(ytdl.extract_info, url=data['webpage_url'], download=False)
        data = await loop.run_in_executor(None, to_run)

        return cls(discord.FFmpegPCMAudio(data['url']), data=data, requester=requester)


class MusicPlayer:


    __slots__ = ('bot', '_guild', '_channel', '_cog', 'queue', 'next', 'current', 'np', 'volume')

    def __init__(self, ctx):
        self.bot = ctx.bot
        self._guild = ctx.guild
        self._channel = ctx.channel
        self._cog = ctx.cog

        self.queue = asyncio.Queue()
        self.next = asyncio.Event()

        self.np = None  # Now playing message
        self.volume = .5
        self.current = None

        ctx.bot.loop.create_task(self.player_loop())

    async def player_loop(self):
        """Our main player loop."""
        await self.bot.wait_until_ready()

        while not self.bot.is_closed():
            self.next.clear()

            try:
                # Wait for the next song. If we timeout cancel the player and disconnect...
                async with timeout(300):  # 5 minutes...
                    source = await self.queue.get()
            except asyncio.TimeoutError:
                return self.destroy(self._guild)

            if not isinstance(source, YTDLSource):
                # Source was probably a stream (not downloaded)
                # So we should regather to prevent stream expiration
                try:
                    source = await YTDLSource.regather_stream(source, loop=self.bot.loop)
                except Exception as e:
                    await self._channel.send(f'There was an error processing your song.\n'
                                             f'```css\n[{e}]\n```')
                    continue

            source.volume = self.volume
            self.current = source

            self._guild.voice_client.play(source, after=lambda _: self.bot.loop.call_soon_threadsafe(self.next.set))
            embed = discord.Embed(title="Now playing", description=f"[{source.title}]({source.web_url}) [{source.requester.mention}]", color=discord.Color.green())
            self.np = await self._channel.send(embed=embed)
            await self.next.wait()

            # Make sure the FFmpeg process is cleaned up.
            source.cleanup()
            self.current = None

    def destroy(self, guild):
        """Disconnect and cleanup the player."""
        return self.bot.loop.create_task(self._cog.cleanup(guild))


class Music(commands.Cog):
    """Music related commands."""

    __slots__ = ('bot', 'players')

    def __init__(self, bot):
        self.bot = bot
        self.players = {}

    async def cleanup(self, guild):
        try:
            await guild.voice_client.disconnect()
        except AttributeError:
            pass

        try:
            del self.players[guild.id]
        except KeyError:
            pass

    async def __local_check(self, ctx):
        """A local check which applies to all commands in this cog."""
        if not ctx.guild:
            raise commands.NoPrivateMessage
        return True

    async def __error(self, ctx, error):
        """A local error handler for all errors arising from commands in this cog."""
        if isinstance(error, commands.NoPrivateMessage):
            try:
                return await ctx.send('This command can not be used in Private Messages.')
            except discord.HTTPException:
                pass
        elif isinstance(error, InvalidVoiceChannel):
            await ctx.send('Error connecting to Voice Channel. '
                           'Please make sure you are in a valid channel or provide me with one')

        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)

    def get_player(self, ctx):
        """Retrieve the guild player, or generate one."""
        try:
            player = self.players[ctx.guild.id]
        except KeyError:
            player = MusicPlayer(ctx)
            self.players[ctx.guild.id] = player

        return player

    @cog_ext.cog_slash(name='join', description="connects to voice")
    async def connect_(self, ctx:SlashContext, *, channel: discord.VoiceChannel=None):

        if not channel:
            try:
                channel = ctx.author.voice.channel
            except AttributeError:
                embed = discord.Embed(title="", description="No channel to join. Please call `.join` from a voice channel!!!", color=discord.Color.green())
                await ctx.send(embed=embed)
                raise InvalidVoiceChannel('No channel to join. Please either specify a valid channel or join one.')

        vc = ctx.voice_client

        if vc:
            if vc.channel.id == channel.id:
                return
            try:
                await vc.move_to(channel)
            except asyncio.TimeoutError:
                raise VoiceConnectionError(f'Moving to channel: <{channel}> timed out.')
        else:
            try:
                await channel.connect()
            except asyncio.TimeoutError:
                raise VoiceConnectionError(f'Connecting to channel: <{channel}> timed out.')

        await ctx.send(f'**Joined `{channel}`**')

    @cog_ext.cog_slash(name='play', description="streams music")
    async def play_(self, ctx:SlashContext, *, search: str):

        await ctx.defer()

        vc = ctx.voice_client

        if not vc:
            await ctx.invoke(self.connect_)

        player = self.get_player(ctx)

        # If download is False, source will be a dict which will be used later to regather the stream.
        # If download is True, source will be a discord.FFmpegPCMAudio with a VolumeTransformer.
        source = await YTDLSource.create_source(ctx, search, loop=self.bot.loop, download=False)

        await player.queue.put(source)
    
    @cog_ext.cog_slash(name='lofi', description="plays lofi")
    async def lofi_(self, ctx:SlashContext):
        await ctx.defer()
        random.shuffle(lofi_url)
        vc = ctx.voice_client

        if not vc:
            await ctx.invoke(self.connect_)

        player = self.get_player(ctx)

        # If download is False, source will be a dict which will be used later to regather the stream.
        # If download is True, source will be a discord.FFmpegPCMAudio with a VolumeTransformer.
        for url in lofi_url:
          source = await YTDLSource.create_source(ctx, url, loop=self.bot.loop, download=False)
          await player.queue.put(source)
    

    @cog_ext.cog_slash(name="favadd",description="add music links to a private playlist")
    async def favadd_(self,ctx,*,search:str):
      
      authid = ctx.author.id
      r = yt.YoutubeSearch(search,1).to_dict()
      r = str(r)
      youtubeid = r[9:20]
      authid = str(authid)
      youtubeid = str(youtubeid)
      title = func.Getyt(f"https://youtube.com/watch?v={youtubeid}")
      

      with open("musicdata.json","r") as jsonfile:
        jsonfile = json.load(jsonfile)
      
      with open("musicdata.json","w") as f:
        if authid in jsonfile:
          ytiddict = {"id":youtubeid,"title" : title,"index":len(jsonfile[authid])}
          jsonfile[authid].append(ytiddict)
          json.dump(jsonfile,f,indent=3)
          await ctx.send(
            embed=discord.Embed(
              title = "your updated playlist",
              description = "\n".join([f"[**`{_['index']} {_['title']}`**](https://youtube.com/watch?v={_['id']})" for _ in jsonfile[authid]]),
              color = discord.Color.blurple())
              )
         
        else:
          jsonfile[authid] = []
          ytiddict = {"id":youtubeid,"title" : title,"index":0}
          jsonfile[authid].append(ytiddict)
          json.dump(jsonfile,f,indent=3)
          await ctx.send(
            embed=discord.Embed(
              title = "your updated playlist",
              description = "\n".join([f"[**`{_['index']} {_['title']}`**](https://youtube.com/watch?v={_['id']})" for _ in jsonfile[authid]]),
              color = discord.Color.blurple())
              )
          
          
      await ctx.author.send(f"link: >https://youtube.com/watch?v={youtubeid}<")
    



    @cog_ext.cog_slash(name="favdel",description="deletes the given index of your private playlist")
    async def favdel_(self,ctx,index:int):
      try:
        authid = ctx.author.id
        authid = str(authid)

        with open("musicdata.json","r") as jsonfile:
          jsonfile = json.load(jsonfile)
        
        with open("musicdata.json","w") as f:
  
            jsonfile[authid].pop(index)
            json.dump(jsonfile,f,indent=3) 
            await ctx.send(
            embed=discord.Embed(
              title = "your current playlist after deletion",
              description = "\n".join([f"[**`{_['index']} {_['title']}`**](https://youtube.com/watch?v={_['id']})" for _ in jsonfile[authid]]),
              color = discord.Color.blurple())
              )
      except:
        pass 
        await ctx.send("some error occured \:(")
      

    @cog_ext.cog_slash(name="faview",description="see your private playlist")
    async def faview_(self,ctx):
      authid = str(ctx.author.id)
      with open("musicdata.json","r") as jsonfile:
        jsonfile = json.load(jsonfile)

         
      

     
        if authid in jsonfile:
            await ctx.send(
            embed=discord.Embed(
              title = "your playlist",
              description = "\n".join([f"[**`{_['index']} {_['title']}`**](https://youtube.com/watch?v={_['id']})" for _ in jsonfile[authid]]),
              color = discord.Color.blurple())
              )

          
        else:
          await ctx.send("first add a song!")
    @cog_ext.cog_slash(name='favplay', description="plays favurites")
    async def favplay_(self, ctx:SlashContext):
      try:
          await ctx.defer()
          authid = str(ctx.author.id)
          with open("musicdata.json","r") as jsonfile:
            jsonfile = json.load(jsonfile)
            playlist =  jsonfile[authid]
            random.shuffle(playlist)
            
            vc = ctx.voice_client

            if not vc:
              await ctx.invoke(self.connect_)

            player = self.get_player(ctx)

          # If download is False, source will be a dict which will be used later to regather the stream.
          # If download is True, source will be a discord.FFmpegPCMAudio with a VolumeTransformer.
            for url in playlist:
              source = await YTDLSource.create_source(ctx, f"https://youtube.com/watch?v={url['id']}", loop=self.bot.loop, download=False)
              await player.queue.put(source)
      except Exception as e:
        print(e)
        





    @cog_ext.cog_slash(name='pause', description="pauses music")
    async def pause_(self, ctx:SlashContext):
        """Pause the currently playing song."""
        vc = ctx.voice_client

        if not vc or not vc.is_playing():
            embed = discord.Embed(title="", description="I am currently not playing anything", color=discord.Color.green())
            return await ctx.send(embed=embed)
        elif vc.is_paused():
            return

        vc.pause()
        await ctx.send("Paused ⏸️")

    @cog_ext.cog_slash(name='resume', description="resumes music")
    async def resume_(self, ctx:SlashContext):
        """Resume the currently paused song."""
        vc = ctx.voice_client

        if not vc or not vc.is_connected():
            embed = discord.Embed(title="", description="I'm not connected to a voice channel", color=discord.Color.green())
            return await ctx.send(embed=embed)
        elif not vc.is_paused():
            return

        vc.resume()
        await ctx.send("Resuming ⏯️")

    @cog_ext.cog_slash(name='skip', description="skips to next song in queue")
    async def skip_(self, ctx:SlashContext):
        """Skip the song."""
        vc = ctx.voice_client

        if not vc or not vc.is_connected():
            embed = discord.Embed(title="", description="I'm not connected to a voice channel", color=discord.Color.green())
            return await ctx.send(embed=embed)

        if vc.is_paused():
            pass
        elif not vc.is_playing():
            return

        vc.stop()
    
    @cog_ext.cog_slash(name='remove', description="removes specified song from queue")
    async def remove_(self, ctx:SlashContext, posistion : int=None):
        """Removes specified song from queue"""

        vc = ctx.voice_client

        if not vc or not vc.is_connected():
            embed = discord.Embed(title="", description="I'm not connected to a voice channel", color=discord.Color.green())
            return await ctx.send(embed=embed)

        player = self.get_player(ctx)
        if pos == None:
            player.queue._queue.pop()
        else:
            try:
                s = player.queue._queue[pos-1]
                del player.queue._queue[pos-1]
                embed = discord.Embed(title="", description=f"Removed [{s['title']}]({s['webpage_url']}) [{s['requester'].mention}]", color=discord.Color.green())
                await ctx.send(embed=embed)
            except:
                embed = discord.Embed(title="", description=f'Could not find a track for "{pos}"', color=discord.Color.green())
                await ctx.send(embed=embed)
    
    @cog_ext.cog_slash(name='clear', description="clears entire queue")
    async def clear_(self, ctx:SlashContext):
        """Deletes entire queue of upcoming songs."""

        vc = ctx.voice_client

        if not vc or not vc.is_connected():
            embed = discord.Embed(title="", description="I'm not connected to a voice channel", color=discord.Color.green())
            return await ctx.send(embed=embed)

        player = self.get_player(ctx)
        player.queue._queue.clear()
        await ctx.send('**Cleared**')

    @cog_ext.cog_slash(name='queue', description="shows the queue")
    async def queue_info(self, ctx:SlashContext):
        """Retrieve a basic queue of upcoming songs."""
        vc = ctx.voice_client

        if not vc or not vc.is_connected():
            embed = discord.Embed(title="", description="I'm not connected to a voice channel", color=discord.Color.green())
            return await ctx.send(embed=embed)

        player = self.get_player(ctx)
        if player.queue.empty():
            embed = discord.Embed(title="", description="queue is empty", color=discord.Color.green())
            return await ctx.send(embed=embed)

        seconds = vc.source.duration % (24 * 3600) 
        hour = seconds // 3600
        seconds %= 3600
        minutes = seconds // 60
        seconds %= 60
        if hour > 0:
            duration = "%dh %02dm %02ds" % (hour, minutes, seconds)
        else:
            duration = "%02dm %02ds" % (minutes, seconds)

        # Grabs the songs in the queue...
        upcoming = list(itertools.islice(player.queue._queue, 0, int(len(player.queue._queue))))
        fmt = '\n'.join(f"`{(upcoming.index(_)) + 1}.` [{_['title']}]e({_['webpage_url']}) | `Requested by: {_['requester']}`\n" for _ in upcoming)
        fmt = f"\n__Now Playing__:\n[{vc.source.title}]({vc.source.web_url}) | `Requested by: {vc.source.requester}`\n\n__Up Next:__\n" + fmt + f"\n**{len(upcoming)} songs in queue**"
        embed = discord.Embed(title=f'Queue for {ctx.guild.name}', description=fmt, color=discord.Color.green())
        embed.set_footer(text=f"{ctx.author.display_name}", icon_url=ctx.author.avatar_url)

        await ctx.send(embed=embed)

        await asyncio.sleep(3)

        

    @cog_ext.cog_slash(name='np', description="shows the current playing song")
    async def now_playing_(self, ctx:SlashContext):
        """Display information about the currently playing song."""
        vc = ctx.voice_client

        if not vc or not vc.is_connected():
            embed = discord.Embed(title="", description="I'm not connected to a voice channel", color=discord.Color.green())
            return await ctx.send(embed=embed)

        player = self.get_player(ctx)
        if not player.current:
            embed = discord.Embed(title="", description="I am currently not playing anything", color=discord.Color.green())
            return await ctx.send(embed=embed)
        
        seconds = vc.source.duration % (24 * 3600) 
        hour = seconds // 3600
        seconds %= 3600
        minutes = seconds // 60
        seconds %= 60
        if hour > 0:
            duration = "%dh %02dm %02ds" % (hour, minutes, seconds)
        else:
            duration = "%02dm %02ds" % (minutes, seconds)

        embed = discord.Embed(title="", description=f"[{vc.source.title}]({vc.source.web_url}) [{vc.source.requester.mention}] | `{duration}`", color=discord.Color.green())
        embed.set_author(icon_url=self.bot.user.avatar_url, name=f"Now Playing 🎶")
        await ctx.send(embed=embed)

    @cog_ext.cog_slash(name='volume', description="changes volume")
    async def change_volume(self, ctx:SlashContext, *, vol: float=None):
        """Change the player volume.
        Parameters
        ------------
        volume: float or int [Required]
            The volume to set the player to in percentage. This must be between 1 and 100.
        """
        vc = ctx.voice_client

        if not vc or not vc.is_connected():
            embed = discord.Embed(title="", description="I am not currently connected to voice", color=discord.Color.green())
            return await ctx.send(embed=embed)
        
        if not vol:
            embed = discord.Embed(title="", description=f"🔊 **{(vc.source.volume)*100}%**", color=discord.Color.green())
            return await ctx.send(embed=embed)

        if not 0 < vol < 101:
            embed = discord.Embed(title="", description="Please enter a value between 1 and 100", color=discord.Color.green())
            return await ctx.send(embed=embed)

        player = self.get_player(ctx)

        if vc.source:
            vc.source.volume = vol / 100

        player.volume = vol / 100
        embed = discord.Embed(title="", description=f'**`{ctx.author}`** set the volume to **{vol}%**', color=discord.Color.green())
        await ctx.send(embed=embed)

    @cog_ext.cog_slash(name='leave', description="stops music and disconnects from voice")
    async def leave_(self, ctx:SlashContext):
        """Stop the currently playing song and destroy the player.
        !Warning!
            This will destroy the player assigned to your guild, also deleting any queued songs and settings.
        """
        vc = ctx.voice_client

        if not vc or not vc.is_connected():
            embed = discord.Embed(title="", description="I'm not connected to a voice channel", color=discord.Color.green())
            return await ctx.send(embed=embed)

     
        await ctx.send('**Successfully disconnected**')

        await self.cleanup(ctx.guild)
      


def setup(bot):
    bot.add_cog(Music(bot))
    bot.add_cog(General(bot))