import discord
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

client = discord.Client()

@client.event
async def on_ready():
    print("Logamos com sucesso como {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
      return
      
    if message.content.startswith('$') or message.content.startswith("$ajuda"):
      await message.channel.send('**COMANDOS** \n$play \n$gemido \n$conversa \n$meme \n$loli')

client.run(os.environ.get('TOKEN'))