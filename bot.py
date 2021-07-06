from private import env
from discord.ext import commands
import discord
from utils import *
import json
import os

ENV = env.env() # Environment

intents = discord.Intents.default() # Gets intents
intents.members = True # Turns on members intent
intents.guilds = True # Turns on guilds intent



with open('bot.json') as f:
    CONFIG: dict = json.load(f)

client = commands.Bot(command_prefix = get_prefix, intents = intents)
client.remove_command('help') # Removes the premade help command

dev_ids: list = [] # List representing developer IDs

vals = {
    "config": CONFIG
}

client.rc_vals = vals # Set the vals dict


for filename in os.listdir('./commands'): # Iterate through commands directory
    if filename.endswith('.py'): # If the file is a python file
        client.load_extension(f'commands.{filename[:-3]}') # Load the extension
        print(f'Successfully loaded commands.{filename[:-3]}')

def run():
    client.run(ENV.token) # Run the bot using token from env class