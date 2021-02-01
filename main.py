import discord
import os
import requests
import json
import random
from replit import db
from keep_alive import keep_alive

client = discord.Client()

starter_init_phrases = ['LET\'S HUNT!']
hype_phrases = [
  'The hunt is on, ',
  'Hope you have insurance! ',
  'Butts, butts, butts! ',
  'Tell all your palicoes, ']

if 'awake' not in db.keys():
  db['awake'] = True

def get_joke():
  response = requests.get(
    "https://icanhazdadjoke.com/",
    headers={
      'User-Agent':'discord bot (darenkmeans@gmail.com)',
      'Accept':'application/json'
    }
  )
  json_data = json.loads(response.text)
  joke = json_data['joke']
  return(joke)

def update_init(phrase):
  if 'initialisers' in db.keys():
    initialisers = db['initialisers']
    initialisers.append(phrase)
    db['initialisers'] = initialisers

  else:
    db['initialisers'] = [phrase]

def delete_init(idx):
  initialisers = db['initialisers']
  if len(initialisers) > idx:
    del initialisers[idx]
    db['initialisers'] = initialisers

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    usr = message.author
    if usr == client.user:
        return

    msg = message.content

    if db['awake']:
      if msg.startswith('!joke'):
        joke = get_joke()
        await message.channel.send(joke)

      options = starter_init_phrases
      if 'initialisers' in db.keys():
        options = options + db['initialisers']

      if any(phrase in msg for phrase in options):
        await message.channel.send('@here, ' + random.choice(hype_phrases) + '{0} is starting a hunt'.format(usr.mention))

      if msg.startswith('!new'):
        init_msg = msg.split('!new ',1)[1]
        update_init(init_msg)
        await message.channel.send('New initialiser added, great jorb.')

      if msg.startswith('!del'):
        init_list = []
        if 'initialisers' in db.keys():
          idx = int(msg.split('!del',1)[1])
          delete_init(idx)
          init_list = db['initialisers']
        await message.channel.send(init_list)

      if msg.startswith('!list'):
        initialisers = []
        if 'initialisers' in db.keys():
          initialisers = db['initialisers']
        await message.channel.send(initialisers)

    if msg.startswith('!guildbot'):
      value = msg.split('!guildbot ',1)[1]

      if value.lower() == 'wake up':
        db['awake'] = True
        await message.channel.send('I\'m awake now!')
      else:
        db['awake'] = False
        await message.channel.send('Aight imma head out...')

keep_alive()
client.run(os.getenv('TOKEN'))