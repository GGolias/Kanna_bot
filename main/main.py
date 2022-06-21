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
activity = discord.Activity(name='!!comandos', type=discord.ActivityType.watching)
# Define o prefixo dos comandos
client = commands.Bot(command_prefix='!!', intents = intents, activity=activity)

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
  
    match datetime.now().strftime("%A"):
      case "Monday":
        await channel.send("Odeio segundas. :tired_face:")
      case "Tuesday":
        await channel.send("A semana so esta começando. :weary:")
      case "Wednesday":
        await channel.send("Ainda no meio da semana. :confused:")
      case "Thursday":
        await channel.send("Tá chegando a sexta! :slight_smile:")
      case "Friday":
        await channel.send("Final de semana só lol e todynho! :sunglasses:")
      case "Saturday":
        await channel.send("Bora encher o rabo de cachaçaaaaa! :laughing:")
      case "Monday":
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
  await channel.send(file=discord.File('welcomeLolibot.gif'), content=f"Seja bem Vindo(a)! {member.mention} Me ajude a sair do porão!")


# Se despedindo
@client.event
async def on_member_remove(member):
  channel = await find_channel(member.guild)
  await channel.send(file=discord.File('goodbyeLolibot.gif'), content=f"Espero que tenha gostado de tomar uma breja comigo {member.mention}... eh digo suco hehe")


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
 
  embed.add_field(name='!!loli <texto>', value='vou conversar com você até altas horas.', inline=False)
  embed.add_field(name='!!reddit <subreddit>', value=' vou enviar um post do subreddit que voce quiser, sem parametro envio um meme do r/shitposting.', inline=False)
  embed.add_field(name='!!codigo', value='por favor! esse nao!', inline=False)
  embed.add_field(name='!!waifu <tipo>  <categoria>', value='nsfw ou sfw e seu fetiche.', inline=False)
  embed.add_field(name='!!ohayo', value='vou dar um bom dia bem animado pra voce!', inline=False)
  embed.add_field(name='!!gemido', value='vou dar um gemido bem gostoso!', inline=False)
  embed.add_field(name='!!sexta', value='hino da sexta-feira.', inline=False)

  embed.set_footer(text='Fim.')

  await ctx.send(embed=embed)


# Falar com o Bot
@client.command()
async def loli(ctx, msg):
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
  await ctx.reply(file=discord.File('shyLolibot.gif'), mention_author=True)
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
async def ohayo(ctx):
  if ctx.author.voice:
    channel = ctx.message.author.voice.channel
    voice = await channel.connect()
    source = FFmpegPCMAudio('ohayo.mp3')
    player = voice.play(source)
    await asyncio.sleep(9)
    await ctx.guild.voice_client.disconnect()
  else:
    await ctx.reply("Como que eu vou saber qual canal entrar? SEU TAPADO! :angry: entra em algum ai.", mention_author=True)


# Entra em um Canal de Voz e da um gemidão de anime
@client.command(pass_content = True)
async def gemido(ctx):
  if ctx.author.voice:
    channel = ctx.message.author.voice.channel
    voice = await channel.connect()
    source = FFmpegPCMAudio('gemido.mp3')
    player = voice.play(source)
    await asyncio.sleep(2)
    await ctx.guild.voice_client.disconnect()
  else:
    await ctx.reply("Como que eu vou saber qual canal entrar? SEU TAPADO! :angry: entra em algum ai.", mention_author=True)


# Entra em um canal de voz e toca filosofias de chatuba
@client.command(pass_content = True)
async def sexta(ctx):
  if ctx.author.voice:
    channel = ctx.message.author.voice.channel
    voice = await channel.connect()
    source = FFmpegPCMAudio('sexta.mp3')
    player = voice.play(source)
    await asyncio.sleep(128)
    await ctx.guild.voice_client.disconnect()
  else:
    await ctx.reply("Como que eu vou saber qual canal entrar? SEU TAPADO! :angry: entra em algum ai.", mention_author=True)


# Sai de um Canal de voz
@client.command(pass_content = True)
async def leave(ctx):
  if ctx.voice_client:
    await ctx.guild.voice_client.disconnect()
  else:
    await ctx.reply("Tô ai não! seu tobô :rage:", mention_author=True)


if __name__ == '__main__':
  client.run(os.environ.get('TOKEN'))
