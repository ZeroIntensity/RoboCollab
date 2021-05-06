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
client.add_cog(CreateCollab(client))
client.add_cog(Listeners(client, gmd, ENV, startingprefix))
client.add_cog(Set_Prefix(client))
client.add_cog(AddPart(client))
client.add_cog(Invite(client))
client.add_cog(Delete(client))
client.add_cog(Join(client))
client.add_cog(Link(client, gmd))
client.add_cog(Collabs(client))
'''

@gmd.listen_for("message", delay=5.0) # Listens for a GD event
async def on_message(message: gd.message.Message):
  with open("private/users.json", "r") as f:
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
        with open("private/users.json", "w") as f:
          json.dump(users, f) # Dump the json data
        break
      await message.read()
      if str(message.body).lower() == 'unlink':
        await message.reply('Successfully unlinked!') # Reply to the message on GD
        del users[i]
        with open("private/users.json", "w") as f:
          json.dump(users, f) # Dump the json data
        break
'''
    

@client.command()
async def info(ctx):
  await normalembed(ctx, 'RoboCollab Info', f'**Language:** `Python {python_version()}`\n**RoboCollab Version:** `V7 {version}`\n**Servers:** `{len(client.guilds)}`\n**Users:** `{len(client.users)}`\n\n**Created by [ZeroIntensity](https://zintensity.net)**\n**RoboCollab\'s [GitHub](https://github.com/ZeroIntensity/RoboCollab)**')


@client.command(name="eval") # totally not stolen yes
async def eval_fn(ctx, *, code):
          if not str(ctx.author.id) == '736038441384542268':
            await error(ctx, 'You cannot run this command.')
            return
          language_specifiers = ["python", "py", "javascript", "js", "html", "css", "php", "md", "markdown", "go", "golang", "c", "c++", "cpp", "c#", "cs", "csharp", "java", "ruby", "rb", "coffee-script", "coffeescript", "coffee", "bash", "shell", "sh", "json", "http", "pascal", "perl", "rust", "sql", "swift", "vim", "xml", "yaml"]
          loops = 0
          while code.startswith("`"):
              code = "".join(list(code)[1:])
              loops += 1
              if loops == 3:
                  loops = 0
                  break
          for language_specifier in language_specifiers:
              if code.startswith(language_specifier):
                  code = code.lstrip(language_specifier)
          while code.endswith("`"):
              code = "".join(list(code)[0:-1])
              loops += 1
              if loops == 3:
                  break
          code = "\n".join(f"    {i}" for i in code.splitlines()) #Adds an extra layer of indentation
          code = f"async def eval_expr():\n{code}" #Wraps the code inside an async function
          def send(text): #Function for sending message to discord if code has any usage of print function
              client.loop.create_task(ctx.send(text))
          env = {
                "bot": client,
                "client": client,
                "ctx": ctx,
                "print": send,
                "_author": ctx.author,
                "_message": ctx.message,
                "_channel": ctx.channel,
                "_guild": ctx.guild,
                "_me": ctx.me
          }
          env.update(globals())
          try:
                exec(code, env)
                eval_expr = env["eval_expr"]
                result = await eval_expr()
                if result:
                    await ctx.send(result)
          except:
                await ctx.send(f"```py\n{traceback.format_exc()}```")


@client.command()
async def help(ctx, args = None):
    prefix = await grab_prefix(ctx) # Get the guild prefix
    if str(args).lower() == 'main': # Check for main argument
        embed = await customembed(ctx, 'Help', f'**Main Commands**\nUse `{prefix}help <command>` for more help on a command.')
        embed.add_field(name="Ping", value=f"``{prefix}ping``")
        await ctx.send(embed=embed)
        return
    embed = await customembed(ctx, 'Help', 'Please select a category') # Sent if no/invalid argument is specified
    embed.add_field(name="Main Commands", value=f"``{prefix}help main``")
    embed.add_field(name="GD Commands", value=f"``{prefix}help gd``")
    embed.add_field(name="Collab Commands", value=f"``{prefix}help collab``")
    await ctx.send(embed=embed)



client.run(ENV.token) # Run the bot using token from .env file
