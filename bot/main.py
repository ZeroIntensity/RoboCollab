"""
MIT License

Copyright (c) 2021 ZeroIntensity

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import discord
import sqlite3
from discord.ext import commands
import json
from private import env
from utils import *
from pathlib import Path
import os
import traceback

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
    "config": CONFIG
}

client.rc_vals = vals # Set the vals dict

# Command for handling extensions within discord
@client.command()
async def extension(ctx, operation, extension = None):
    if check_rc_perms(ctx.author.id, "developer", CONFIG): # Check if they have needed perms
        if operation == "reload_all":
            msg = reload_cogs()
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



for filename in os.listdir('./commands'): # Iterate through commands directory
    if filename.endswith('.py'): # If the file is a python file
        client.load_extension(f'commands.{filename[:-3]}') # Load the extension
        print(f'Successfully loaded commands.{filename[:-3]}')


client.run(ENV.token) # Run the bot using token from env class