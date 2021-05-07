# Main file.

# All of these are here to make managing dependencies easier
import discord # Import discord.py
from discord.ext import commands # To initialize the bot client
from discord.ext import tasks # For autostatus
import gd # Import gd.py
import os # Stuff for file mangagement and such
import dotenv # Needed to load the .env file
import json # Used for JSON
import asyncio # Import asyncio ~ Needed for autostatus
from pytube import YouTube # For handling youtube links. would use bs4 but this is easier lmao
import jsondb # Thing I made for better handling json
import traceback # For error handling
import string # For getting alphabet
from platform import python_version # For python version
from utils import *
from commands import *
from private import env

ENV = env.env()

startingprefix = '//' # Default prefix for when the bot joins a guild

intents = discord.Intents.default() # Gets intents
intents.members = True # Turns on members intent
intents.guilds = True # Turns on guilds intent

client = commands.Bot(command_prefix = get_prefix, intents = intents) # Initializes the bot client

gmd = gd.Client() # Initializes the gd client
client.gmd = gmd # Attatch bot to gd client
version = '1.0.0'

client.remove_command('help') # Removes the premade help command
client.add_cog(CreateCollab(client, jsondb)) # Adds createcollab command
client.add_cog(Listeners(client, gmd, ENV, startingprefix)) # Adds all the listeners (on_guild_join, on_ready, etc)
client.add_cog(Set_Prefix(client)) # Adds set_prefix command
client.add_cog(AddPart(client, jsondb)) # Adds addpart command
client.add_cog(Invite(client, jsondb)) # Adds invite command
client.add_cog(Delete(client, jsondb)) # Adds delete command
client.add_cog(Join(client, jsondb)) # Adds join command
client.add_cog(Link(client, gmd)) # Adds link command
client.add_cog(Collabs(client)) # Adds collabs command
client.add_cog(Help(client)) # Adds help command
client.add_cog(Eval(client)) # Adds eval command
client.add_cog(Json(client)) # Adds JSON command
client.add_cog(Info(client, version)) # Adds Info command


@gmd.listen_for("message", delay=5.0) # Listens for a GD event
async def on_message(message: gd.message.Message):
  with open(f"{get_private_folder()}users.json", "r") as f:
    users = json.load(f) # Load the users json
  for i in users: # Iterates through every key in the json
    if users[i].get('account_id') == message.author.account_id: # Check if the current key has an account ID of the sender
      await message.read() # Reads the message
      if str(message.body).lower() == 'verify':
        if not users[i]['linktype'] == 'verified':
          await message.reply(f'Verified as {client.get_user(int(str(i)))}! If you would like to unlink, please message "unlink" to this account') # Reply to the message on GD
        else: # If they are already verified
          await message.reply(f'You are already linked! If you would like to unlink, please message "unlink" to this account.') # Reply to the message on GD
          break
        users[i]['linktype'] = 'verified' # Sets the linktype to verified
        with open(f"{get_private_folder()}users.json", "w") as f:
          json.dump(users, f) # Dump the json data
        break
      await message.read()
      if str(message.body).lower() == 'unlink':
        await message.reply('Successfully unlinked!') # Reply to the message on GD
        del users[i]
        with open(f"{get_private_folder()}users.json", "w") as f:
          json.dump(users, f) # Dump the json data
        break

    
client.run(ENV.token) # Run the bot using token from env class
