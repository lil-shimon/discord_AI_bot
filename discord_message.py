import discord
import config
from prsaw import RandomStuffV2

TOKEN = config.DISCORD_TOKEN
client = discord.Client()
api_key = config.API_KEY
rs = RandomStuffV2()


@client.event
async def on_ready():
    print('Ready')

@client.event
async def on_message(message):
    if message.author.bot:
        return

    if client.user in message.mentions:
        response = rs.get_ai_response(message.content)
        await message.reply(response)

client.run(TOKEN)

