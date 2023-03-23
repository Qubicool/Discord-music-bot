import discord
from discord import *
import youtube_dl
import asyncio

token = "your token here"
intents = discord.Intents.all()
client = discord.Client(intents=intents)

voice_clients = {}
yt_dl_opts = {'format': 'bestaudio/best'}
ytdl = youtube_dl.YoutubeDL(yt_dl_opts)
ffmpeg_options = {'options': '-vn'}

#message when the bot gets run
@client.event
async def on_ready():
    print(f"Bot logged in as {client.user}")

#
@client.event
async def on_message(msg):
    if msg.content.startswith("!play"):
        try:
            voice_client = await msg.author.voice.channel.connect()
            voice_clients[voice_client.guild.id] = voice_client
        except Exception as err:
            print(err)
        try:
            url = msg.content.split()[1]
            loop = asyncio.get_event_loop()
            data = await loop.run_in_executor(None,lambda: ytdl.extract_info(url, download=False))
            song = data['url']
            player = discord.FFmpegPCMAudio(song, **ffmpeg_options)
            voice_clients[msg.guild.id].play(player)
        except Exception as err:
            print(err)
    #pause
    if msg.content.startswith("!pause"):
        try:
            voice_clients[msg.guild.id].pause()
            await msg.channel.send("Music paused!")
        except Exception as err:
            print(err)
    #resume
    if msg.content.startswith("!resume"):
        try:
            voice_clients[msg.guild.id].resume()
            await msg.channel.send("Music resumed!")
        except Exception as err:
            print(err)
    #stop
    if msg.content.startswith("!stop"):
        try:
            voice_clients[msg.guild.id].stop()
            await msg.channel.send("Music stopped, let's listen next!")
        except Exception as err:
            print(err)
    if msg.content.startswith("!bye"):
        try:
            voice_clients[msg.guild.id].stop()
            await msg.channel.send("Paka!")
            await voice_clients[msg.guild.id].disconnect()
        except Exception as err:
            print(err)


client.run(token)
