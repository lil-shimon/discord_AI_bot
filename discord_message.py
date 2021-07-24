import discord
import config

TOKEN = config.DISCORD_TOKEN
client = discord.Client()

@client.event
async def on_ready():
    print('Ready')

@client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content == 'hello':
        await message.channel.send('hello world')

client.run(TOKEN)

