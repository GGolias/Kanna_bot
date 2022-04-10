# Importando Bibliotecas
import discord
import os
import requests
from dotenv import load_dotenv, find_dotenv
from discord.ext import commands
from discord import FFmpegPCMAudio
from time import sleep

# Carrega o arquivo .env
load_dotenv(find_dotenv())

intents = discord.Intents.default()
intents.members = True

# Define o prefixo dos comandos
client = commands.Bot(command_prefix='!!', intents = intents)

# ==================================== Eventos ====================================

# Status do Bot
@client.event
async def on_ready():
    print("Logamos com sucesso como {0.user}".format(client))

# Efetua boas vindas
@client.event
async def on_member_join(member):
  channel = client.get_channel(962462461171228765)
  await channel.send(f"Seja bem Vindo(a)! {member.mention} Me ajude a sair do porão!")

# Se despede 
@client.event
async def on_member_remove(member):
  channel = client.get_channel(962462461171228765)
  await channel.send(f"Espero que tenha gostado de tomar uma breja comigo {member.mention}... eh digo suco hehe")

# ==================================== Comandos ====================================

# Listar comandos
@client.command()
async def comandos(ctx):
  await ctx.send('**COMANDOS** \n!!ohayo - dou um bom dia bem animado pra você! \n!!gemido - vou gemer no seu ouvido senpai-kun.\n!!loli - vou conversar com você até altas horas.')

# Falar com o Bot
@client.command()
async def loli(ctx, msg):
  loli_conversa_token = os.environ.get('RAPIDAPIKEYLOLI')
  boturl = "https://waifu.p.rapidapi.com/path"
  
  # Definindo caracteristicas especificas da convesa
  user_id = ctx.author.id
  de = ctx.author
  para = "LOLI_BOTKKKKKKK"
  situacao = "LOLI_BOTKKKKKKK é uma Loli e está presa em um porão."

  querystring = {"user_id":user_id,"message":msg,"from_name":de,"to_name":para,"situation":situacao,"translate_from":"pt","translate_to":"pt"}

  payload = {}
  headers = {
    "content-type": "application/json",
    "X-RapidAPI-Host": "waifu.p.rapidapi.com",
    "X-RapidAPI-Key": loli_conversa_token
  }
  response = requests.request("POST", boturl, json=payload, headers=headers, params=querystring)
  
  await ctx.send(response.text)

# Entra em um Canal de Voz e Diz um ohayo bem massa
@client.command(pass_content = True)
async def ohayo(ctx):
  if ctx.author.voice:
    channel = ctx.message.author.voice.channel
    voice = await channel.connect()
    source = FFmpegPCMAudio('ohayo.mp3')
    player = voice.play(source)
    sleep(9)
    await ctx.guild.voice_client.disconnect()
  else:
    await ctx.send("Como que eu vou saber qual canal entrar? SEU TAPADO! entra em algum ai.")

# Entra em um Canal de Voz e da um gemidão de anime
@client.command(pass_content = True)
async def gemido(ctx):
  if ctx.author.voice:
    channel = ctx.message.author.voice.channel
    voice = await channel.connect()
    source = FFmpegPCMAudio('gemido.mp3')
    player = voice.play(source)
    sleep(2)
    await ctx.guild.voice_client.disconnect()
  else:
    await ctx.send("Como que eu vou saber qual canal entrar? SEU TAPADO! entra em algum ai.")

# Sai de um Canal de voz
@client.command(pass_content = True)
async def leave(ctx):
  if ctx.voice_client:
    await ctx.guild.voice_client.disconnect()
  else:
    await ctx.send("Tô ai não! seu tobô!")


client.run(os.environ.get('TOKEN'))