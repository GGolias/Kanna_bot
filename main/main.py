# Importando Bibliotecas
from cmath import e
from email import message
import discord, os, asyncio, requests
from pygame import Color
from dotenv import load_dotenv, find_dotenv
from discord.ext import commands, tasks
from discord import FFmpegPCMAudio
from time import sleep
from datetime import datetime

# Carrega o arquivo .env
load_dotenv(find_dotenv())

intents = discord.Intents.default()
intents.members = True

# Define a atividade do bot
activity = discord.Activity(name='-comandos', type=discord.ActivityType.watching)
# Define o prefixo dos comandos
client = commands.Bot(command_prefix='-', intents = intents, activity=activity)

# ==================================== Eventos ====================================

# Status do Bot
@client.event
async def on_ready():
    print("Logamos com sucesso como {0.user}".format(client))
    msg1.start()


# Message 1
@tasks.loop(hours=24)
async def msg1():

  for guild in client.guilds:
    channel = guild.text_channels[0]
  
    if datetime.now().strftime("%A") == "Monday":  
      await channel.send("Odeio segundas. :tired_face:")

    elif datetime.now().strftime("%A") == "Tuesday":
      await channel.send("A semana so esta começando. :weary:")

    elif datetime.now().strftime("%A") == "Wednesday":
      await channel.send("Ainda no meio da semana. :confused:")

    elif datetime.now().strftime("%A") == "Thursday":
        await channel.send("Tá chegando a sexta! :slight_smile:")

    elif datetime.now().strftime("%A") == "Friday":
        await channel.send("Final de semana só lol e todynho! :sunglasses:")

    elif datetime.now().strftime("%A") == "Saturday":
        await channel.send("Bora encher o rabo de cachaçaaaaa! :laughing:")

    elif datetime.now().strftime("%A") == "Monday":
        await channel.send("Ressaca é foda bixo. :disappointed:")

    response = requests.get("https://meme-api.herokuapp.com/gimme/Woodszin")
    await channel.send("toma ai um meme" + response.json()['url'])


@msg1.before_loop
async def before_msg1():
    for _ in range(60*60*24):  # loop the whole day
        if datetime.now().hour == 6: 
            print('It is time')
            return
        await asyncio.sleep(1)# wait a second before looping again. You can make it more


# Procurando canais de texto
async def find_channel(guild):
  for c in guild.text_channels:
    if not c.permissions_for(guild.me).send_messages:
      continue
    return c


# Efetua boas vindas
@client.event
async def on_member_join(member):
  channel = await find_channel(member.guild)
  await channel.send(file=discord.File('imagens/welcomeLolibot.gif'), content=f"Seja bem Vindo(a)! {member.mention} Me ajude a sair do porão!")


# Se despedindo
@client.event
async def on_member_remove(member):
  channel = await find_channel(member.guild)
  await channel.send(file=discord.File('imagens/goodbyeLolibot.gif'), content=f"Espero que tenha gostado de tomar uma breja comigo {member.mention}... eh digo suco hehe")


# Lendos as mensagens
@client.event
async def on_message(message):
  if message.content.upper() == "F":
    await message.channel.send("F no chat guys :sob:")

  elif message.content.upper() == "PING":
    await message.channel.send("pong?", reference=message)

  else:
    await client.process_commands(message)

# ==================================== Comandos ====================================

# Listar comandos
@client.command()
async def comandos(ctx):
  embed = discord.Embed(
    title = '**COMANDOS**',
    description = 'Aqui está todos o meus comandos.',
    colour = 16761035
  )
  embed.set_author(name='LoliBot', icon_url='https://c.tenor.com/IN6jha4TknYAAAAi/emojify.gif')
  embed.set_thumbnail(url='https://c.tenor.com/3VBAclT6Y0YAAAAd/kanna-universe.gif')
  embed.add_field(name='-loli <texto>', value='vou conversar com você até altas horas. (instavel)', inline=False)
  embed.add_field(name='-reddit <subreddit>', value=' vou enviar um post do subreddit que voce quiser, sem parametro envio um meme do r/shitposting.', inline=False)
  embed.add_field(name='-codigo', value='por favor! esse nao!', inline=False)
  embed.add_field(name='-waifu <tipo> <categoria>', value='nsfw ou sfw e seu fetiche.', inline=False)
  embed.add_field(name='-play <opçao>', value='ohayo, moan e sexta', inline=False)
  embed.add_field(name='-fale <texto>', value='digite algo para eu falar no seu ouvidinho. (instavel)', inline=False)
  embed.add_field(name='-conversa <texto>', value='é tipo o <-loli> junto com o <-fale>. (instavel)', inline=False)
  embed.add_field(name='-leave', value='eu saio do canal de voz', inline=False)
  embed.add_field(name='-convite', value='eu te envio um link pra eu etrar no seu servidor', inline=False)
  embed.set_footer(text='Fim.')
  await ctx.send(embed=embed)


# Falar com o Bot
@client.command()
async def loli(ctx,* , msg):
  loli_conversa_token = os.environ.get('RAPIDAPIKEYLOLI')
  boturl = "https://waifu.p.rapidapi.com/path"

  # Definindo caracteristicas especificas da convesa.
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


# Comando pra postar alguma coisa de um subreddit especificando ou nao.
@client.command()
async def reddit(ctx, subreddit="ShitpostBR"):

  response = requests.get('https://meme-api.herokuapp.com/gimme/' + subreddit)

  if response.status_code != 200:
    await ctx.reply("Sinto muito, nao achei esse subreddit r/" + subreddit + " Tem certeza que está escrito certo?")
  else:
    await ctx.send(response.json()['url'])

# Envia o link do repositorio do git github
@client.command()
async def codigo(ctx):
  await ctx.reply(file=discord.File('imagens/shyLolibot.gif'), mention_author=True)
  await ctx.reply("b-baka :flushed: https://github.com/GGolias/Loli_bot", mention_author=True)
 
 
# Envia uma imagem por padrao de uma waifu
@client.command()
async def waifu(ctx, type="sfw", category="waifu"):

  response = requests.get("https://api.waifu.pics/" + type + "/" + category)
  if response.status_code != 200:
    await ctx.reply("Nao achei nada aqui com os seus fetiches  :sweat:  ")
  else:
    await ctx.send(response.json()['url'])


# Entra em um Canal de Voz e Diz um ohayo bem massa
@client.command(pass_content = True)
async def play(ctx, song):
  if ctx.author.voice:
    channel = ctx.message.author.voice.channel
    voice = await channel.connect()
    if song == 'ohayo':
      source = FFmpegPCMAudio('audios/ohayo.mp3')
    elif song == 'moan':
      source = FFmpegPCMAudio('audios/moan.mp3')
    elif song == 'sexta':
      source = FFmpegPCMAudio('audios/sexta.mp3')
    else:
      await ctx.send('nao entendi, será que escreveu certo?')
    player = voice.play(source)

    while True:
      if voice.is_playing():
        await asyncio.sleep(1)
      else:
        await ctx.guild.voice_client.disconnect()
        break
  else:
    await ctx.reply("Como que eu vou saber qual canal entrar? SEU TAPADO! :angry: entra em algum ai.", mention_author=True)


# Sai de um Canal de voz
@client.command(pass_content = True)
async def leave(ctx):
  if ctx.voice_client: # Caso o usuario esteja em um canal de voz
    await ctx.guild.voice_client.disconnect() # Saia do canal de voz
  else: # Caso o usuario nao esteja em um canal de voz
    await ctx.reply("Tô ai não! seu tobô :rage:", mention_author=True) # Evie essa mensagem


# Gera toca um audio com a fase escrita como parametro.
@client.command()
async def fale(ctx, *, speech): # canal de texto, texto
  api = "https://api.uberduck.ai/speak" # Link da api
  loli_fala_token = "Basic " + os.environ.get('UBERDUCKAPILOLITOKEN') + "=" # Carregando o token para a api

  payload = {
      "voice": "mercy-br", # Voz
      "pace": 1,
      "speech": speech, # Texto para ser processado pela a api e transformado em voz
      "voicemodel_uuid": "0849538e-df9a-44b4-bfe4-948e5048f07e"
  }
  headers = {
      "accept": "application/json",
      "content-type": "application/json",
      "authorization": loli_fala_token # Token para autorizacao
  }

  postResponse = requests.post(api, json=payload, headers=headers) # Posta a mensagem pra ser transformada em fala
  url = "https://api.uberduck.ai/speak-status?uuid=" + postResponse.json()['uuid'] # Pega a uuid do post e gera um request com o link do audio
  headers = {"accept": "application/json"}

  while True:
    path = requests.get(url, headers=headers).json()['path'] # Audio gerado pela a api
    if path == None: # Caso a api ainda nao tenha gerado o audio
      await asyncio.sleep(1) # Espera 1 segundo
    else:
      break

  getResponse = requests.get(url, headers=headers) # Request gerado
  
  if ctx.author.voice: # Caso o usuario tenha entrado em um canal de voz
    channel = ctx.message.author.voice.channel
    voice = await channel.connect() # Conecta no canal de voz
    source = FFmpegPCMAudio(getResponse.json()['path']) # Carrega o arquivo de audio gerado pela a api
    player = voice.play(source) # Toca o audio

    while True:
      if voice.is_playing(): # Caso o audio ainda esteja tocando
        await asyncio.sleep(2) # Espere 2 segundos
      else: # Caso o audio nao esteja tocando
        await asyncio.sleep(2) # Espere 2 segundos
        await ctx.guild.voice_client.disconnect() # Saia do canal de voz
        break 
  else: # Caso o usuario nao tenha entrado em um canal de voz
    await ctx.reply("Nao vou falar nada se tem ninguem pra me escutar.", mention_author=True) # Envie essa mensagem


@client.command()
async def conversa(ctx, *, fala):

  loli_conversa_token = os.environ.get('RAPIDAPIKEYLOLI')
  loli_fala_token = "Basic " + os.environ.get('UBERDUCKAPILOLITOKEN') + "="
  boturl = "https://waifu.p.rapidapi.com/path"

  # Definindo caracteristicas especificas da convesa.
  user_id = ctx.author.id
  de = ctx.author
  para = "LOLI_BOTKKKKKKK"
  situacao = "LOLI_BOTKKKKKKK é uma Loli e está presa em um porão."

  querystring = {"user_id":user_id,"message":fala,"from_name":de,"to_name":para,"situation":situacao,"translate_from":"pt","translate_to":"pt"}

  payload = {}
  headers = {
    "content-type": "application/json",
    "X-RapidAPI-Host": "waifu.p.rapidapi.com",
    "X-RapidAPI-Key": loli_conversa_token
  }
  response = requests.request("POST", boturl, json=payload, headers=headers, params=querystring)

  api = "https://api.uberduck.ai/speak"
  payload = {
      "voice": "mercy-br",
      "pace": 1,
      "speech": response.text,
      "voicemodel_uuid": "0849538e-df9a-44b4-bfe4-948e5048f07e" 
  }
  headers = {
      "accept": "application/json",
      "content-type": "application/json",
      "authorization": loli_fala_token
  }
  postResponse = requests.post(api, json=payload, headers=headers)
  url = "https://api.uberduck.ai/speak-status?uuid=" + postResponse.json()['uuid']
  headers = {"accept": "application/json"}

  while True:
    path = requests.get(url, headers=headers).json()['path']
    if path == None:
      await asyncio.sleep(1)
    else:
      break

  getResponse = requests.get(url, headers=headers)
  
  if ctx.author.voice:
    channel = ctx.message.author.voice.channel
    voice = await channel.connect()
    source = FFmpegPCMAudio(getResponse.json()['path'])
    player = voice.play(source)

    while True:
      if voice.is_playing():
        await asyncio.sleep(2)
      else:
        await asyncio.sleep(2)
        await ctx.guild.voice_client.disconnect()
        break
  else:
    await ctx.reply("Nao vou falar nada se tem ninguem pra me escutar.", mention_author=True)

@client.command()
async def convite(ctx):
  await ctx.send('toma ai seu lindo :relaxed:  \n https://discord.com/oauth2/authorize?client_id=962457964965396520&scope=bot&permissions=8', mention_author=True)

  

if __name__ == '__main__':
  client.run(os.environ.get('TOKEN'))
