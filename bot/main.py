# Main file.

import discord
import sqlite3
from discord.ext import commands
import json
from private import env
from utils import *
from pathlib import Path
import os

ENV = env.env() # Environment

intents = discord.Intents.default() # Gets intents
intents.members = True # Turns on members intent
intents.guilds = True # Turns on guilds intent



SQL('init.sql') # Initializes database, will not run if already initialized

with open('bot.json') as f:
    CONFIG: dict = json.load(f)

client = commands.Bot(command_prefix = get_prefix, intents = intents)
client.remove_command('help') # Removes the premade help command

vals = {
    "client": client,
    "config": CONFIG
}

setattr(client, "rc_vals", vals) # There must be a better way to do this, but I couldn't find it

# Command for handling extensions within discord
@client.command()
async def extension(ctx, operation, extension = None):
    if check_rc_perms(ctx.author.id, "developer", CONFIG): # Check if they have needed perms
        if operation == "reload_all":
            reloaded = []
            for filename in os.listdir('./commands'): # Iterate through commands directory
                if filename.endswith('.py'): # If the file is a python file
                    client.reload_extension(f'commands.{filename[:-3]}') # Load the extension
                    reloaded.append(f'`commands.{filename[:-3]}`')
            msg = "Reloaded "
            for i in reloaded:
                msg += i + ', '
            
            msg = msg[:-2]
            print(msg)
            return await ctx.send(msg)
                    

        if operation == "load": # If the operation is load
            client.load_extension(f'commands.{extension}') # Load the extension
            msg = f'`{extension}` was successfully loaded.' # Define the message to be sent
            print(msg)
            return await ctx.send(msg) # End the command

        elif operation == "unload": # If the operation is unload
            client.unload_extension(f'commands.{extension}') # Unload the extension
            msg = f'`{extension}` was successfully unloaded.' # Define the message to be sent
            print(msg) 
            return await ctx.send(msg) # End the command

        elif operation == "reload": # If the operation is reload
            client.reload_extension(f'commands.{extension}') # Reload the extension
            msg = f'`{extension}` was successfully reloaded.' # Define the message to be sent
            print(msg)
            return await ctx.send(msg) # End the command
    else: 
        await ctx.send('nah bro')
        


for filename in os.listdir('./commands'): # Iterate through commands directory
    if filename.endswith('.py'): # If the file is a python file
        client.load_extension(f'commands.{filename[:-3]}') # Load the extension

client.run(ENV.token) # Run the bot using token from env class