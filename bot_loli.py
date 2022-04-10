import discord
import os
from dotenv import load_dotenv, find_dotenv
from discord.ext import commands

load_dotenv(find_dotenv())

client = commands.Bot(command_prefix='$')

@client.event
async def on_ready():
    print("Logamos com sucesso como {0.user}".format(client))

@client.command()
async def comandos(ctx):
  await ctx.send('**COMANDOS** \n$play \n$gemido \n$conversa \n$meme \n$loli')

@client.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()

@client.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()


client.run(os.environ.get('TOKEN'))