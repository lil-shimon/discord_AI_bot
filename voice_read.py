import discord
from discord.ext import commands

import ffmpeg
from voice_generator import creat_WAV

import config

client = commands.Bot(command_prefix='.')
voice_client = None
TOKEN = config.DISCORD_TOKEN

@client.event
async def on_ready():
    print('Ready!')

# join voice channel
@client.command()
async def join(ctx):
    print('ctx', ctx)
    print('join voice')
    voice = ctx.author.voice.channel
    await voice.connect()

# exit from voice channel
@client.command()
async def bye(ctx):
    print('kill process')
    await ctx.voice_client.disconnect()

@client.event
async def on_message(msg):
    msgclient = msg.guild.voice_client
    print(msgclient)
    if msg.content.startswith('.'):
        pass

    else:
        if msg.guild.voice_client:
            creat_WAV(msg.content)
            src = discord.FFmpegPCMAudio("output.wav")
            msg.guild.voice_client.play(src)
        else:
            pass

    await client.process_commands(msg)

client.run(TOKEN)

