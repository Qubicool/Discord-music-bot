import discord
from discord import *
import youtube_dl
import asyncio

token = "token"
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

queue = []
@client.event
async def on_message(msg):
    if msg.content.startswith("!play"):
        global queue
        try:
            voice_client = await msg.author.voice.channel.connect()
            voice_clients[msg.guild.id] = voice_client
        except Exception as err:
            print(err)
        search_query = " ".join(msg.content.split()[1:]) # возвращает список слов и собирает их в string например !play кто пчелок уважает msg.content.split вернет ["кто","пчелок","уважает"] а вместе .join это соберется в строку "кто пчелок уважает".
        try:
            loop = asyncio.get_event_loop()
            while voice_clients[msg.guild.id].is_playing():
                await asyncio.sleep(1)
            data = await loop.run_in_executor(None, lambda: ytdl.extract_info(f"ytsearch:{search_query}", download=False))
            song = data['entries'][0]['url']
            queue.append(song)
            if len(queue) == 1 and not voice_clients[msg.guild.id].is_playing():
                player = discord.FFmpegPCMAudio(queue[0], **ffmpeg_options)
                voice_clients[msg.guild.id].play(player, after=lambda x: queue.pop(0))
                await msg.channel.send(f"Играет {data['entries'][0]['title']}")
            else:
                await msg.channel.send(f"Добавлено в очередь: {data['entries'][0]['title']} to the queue")
        except Exception as err:
            print(err)
    if msg.content.startswith("!skip"):
        try:
            if voice_clients[msg.guild.id].is_playing():
                voice_clients[msg.guild.id].stop()
                await msg.channel.send("Песня пропущена")
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
