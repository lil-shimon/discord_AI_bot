import discord
import pickle

import random

import config

TOKEN = config.DISCORD_TOKEN
path = '~/project/discord_bot'

client = discord.Client()
word_file = open('words.pickle', 'rb')
words = pickle.load(word_file)

@client.event
async def on_ready():
    print('Ready')

async def reply(message):
    randomizer = random.randint(0, len(words) -1)
    print('randomizer', randomizer)
    reply = f'{message.author.mention} {words[randomizer]}'
    await message.channel.send(reply)

@client.event
async def on_message(message):
    if message.author.bot:
        return

    if client.user in message.mentions:
        await reply(message)

    with open('words.pickle', 'wb') as f:
        pickle.dump(message.content, f)

    print('words list', words)

client.run(TOKEN)

