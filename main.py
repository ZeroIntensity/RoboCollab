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

class colors: # Colors for embeds
  success = 0x80ffa4 # Default

dotenv.load_dotenv() # Load the .env file


async def get_prefix(client, message): # This one is for the command_prefix
  with open("prefixes.json", "r") as f:
    prefixes = json.load(f)
    return prefixes[str(message.guild.id)]

async def grab_prefix(ctx): # This one is used just to grab the guilds prefix in commands
  with open("prefixes.json", "r") as f:
    prefixes = json.load(f) # Load the json
    return prefixes[str(ctx.guild.id)] # Return the prefix

async def normalembed(ctx, title=None, msg=None, col=colors.success): # Normal premade embed
  embed=discord.Embed(color=col)
  embed.timestamp=(ctx.message.created_at)
  if not title == None: # If the title argument isn't specified
    embed.title=title
  if not msg == None: # If the msg argument isn't specified
    embed.description=msg
  embed.set_footer(text='RoboCollab')
  embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
  await ctx.send(embed=embed)

async def customembed(ctx, title=None, msg=None, col=colors.success): # Embed that I can add fields to
  embed=discord.Embed(color=col)
  embed.timestamp=(ctx.message.created_at)
  if not title == None: # If the title argument isn't specified
    embed.title=title
  if not msg == None: # If the msg argument isn't specified
    embed.description=msg
  embed.set_footer(text='RoboCollab')
  embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
  return embed # Returns the embed instead of sending it

startingprefix = '//' # Default prefix for when the bot joins a guild

intents = discord.Intents.default() # Gets intents
intents.members = True # Turns on members intent
intents.guilds = True # Turns on guilds intent

client = commands.Bot(command_prefix = get_prefix, intents = intents) # Initializes the bot client

gmd = gd.Client() # Initializes the gd client
client.gmd = gmd # Attatch bot to gd client
version = '1.0.0'

client.remove_command('help') # Removes the premade help command

async def error(ctx, msg): # Premade embed for invalid arguments
  embed=discord.Embed(color=0xff0000)
  embed.timestamp=(ctx.message.created_at)
  embed.title='Error'
  embed.description=msg # Set the description to the msg argument
  embed.set_footer(text='RoboCollab')
  embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
  await ctx.send(embed=embed) # Send the embed
  return

@client.event # Listen for a bot event
async def on_guild_join(guild): # Do when the bot joins a guild
  with open("prefixes.json", "r") as f:
    prefixes = json.load(f) # Load the prefixes

  prefixes[int(guild.id)] = startingprefix # Sets the default prefix to '//'

  with open("prefixes.json", "w") as f:
    json.dump(prefixes, f) # Dump the json data



@tasks.loop(seconds=10) # Async task that runs every 10 seconds
async def autostatus():
  await asyncio.sleep(10) # Waits 10 seconds to switch statuses
  await client.change_presence(activity=discord.Activity(name=f'{len(client.users)} Users! | {startingprefix}prefix <your new prefix>', type=discord.ActivityType.listening))

  await asyncio.sleep(10) # Also waits 10 seconds
  await client.change_presence(activity=discord.Activity(name=f'{len(client.guilds)} Servers! | {startingprefix}help', type=discord.ActivityType.listening))
  await asyncio.sleep(10) # Again, waits 10 seconds
  await client.change_presence(activity=discord.Activity(name=f'https://robocollab.xyz | {startingprefix}help', type=discord.ActivityType.playing))

@client.event # Listen for a bot event
async def on_ready():
    await gmd.login('RoboCollab', os.getenv('password')) # Logs into GD
    await client.wait_until_ready() # Wait until the bot has logged in
    gd.events.enable(client.loop) # Enable the message listener
    print(f"Logged in as {client.user} ({client.user.id})") # Prints bot tag and ID
    await client.change_presence(activity=discord.Activity(name=f"{len(client.guilds)} Servers! | {startingprefix}help", type=discord.ActivityType.listening))
    autostatus.start() # Starts the autostatus
'''
@gmd.listen_for("message", delay=5.0) # Listens for a GD event
async def on_message(message: gd.message.Message):
  with open("users.json", "r") as f:
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
        with open("users.json", "w") as f:
          json.dump(users, f) # Dump the json data
        break
      await message.read()
      if str(message.body).lower() == 'unlink':
        await message.reply('Successfully unlinked!') # Reply to the message on GD
        del users[i]
        with open("users.json", "w") as f:
          json.dump(users, f) # Dump the json data
        break
'''
    

@client.command()
async def info(ctx):
  await normalembed(ctx, 'RoboCollab Info', f'**Language:** `Python {python_version()}`\n**RoboCollab Version:** `V7 {version}`\n**Servers:** `{len(client.guilds)}`\n**Users:** `{len(client.users)}`\n\n**Created by [ZeroIntensity](https://zintensity.net)**\n**RoboCollab\'s [GitHub](https://github.com/ZeroIntensity/RoboCollab)**')

@client.command() # Define a bot command
async def link(ctx, *, args = None): # Account linking command
  if not args:
    await error('Please specify an account')
    return
  try:
    user = await gmd.find_user(args) # Check to see if the user exists
  except gd.MissingAccess:
    await error('That account doesn\'t exist')
    return
  with open("users.json", "r") as f:
    users = json.load(f)
  x = { # Dict that will be added to the json
    'linktype': 'unverified',
    'account_id': user.account_id
  }
  users[int(ctx.author.id)] = x

  with open("users.json", "w") as f:
    json.dump(users, f) # Dump the json data
  
  await normalembed(ctx, 'Account Link',f'Waiting to link `{args}`. Please message **"verify"** to the account **RoboCollab** on GD.')


@client.command(aliases=['prefix']) # Define a bot command
@commands.has_permissions(manage_guild=True)
async def setprefix(ctx, *, args=None): # Command that changes the guild prefix
  if not args:
    await error(ctx, 'You need to specify a prefix.')
    return
  pre = await grab_prefix(ctx)
  if pre == args: # Checks if its the same as the current prefix
    await error(ctx, 'That is already set as your prefix')
    return
  with open("prefixes.json", "r") as f: # Load the prefixes
    prefixes = json.load(f)
    prefixes [str(ctx.guild.id)] = args # Sets the new prefix
  with open("prefixes.json", "w") as f:
    json.dump(prefixes, f)
  await normalembed(ctx, 'Set Prefix', f'Set the prefix to `{args}`')


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

@client.command(aliases=['create','cc','create_collab'])
@commands.has_permissions(administrator=True)
async def createcollab(ctx, name = None, song = None, difficulty = None):
  database = jsondb.Client('database/')
  valid_difficulties = ['auto','easy','normal','hard','harder','insane','easy demon','medium demon','hard demon','insane demon','extreme demon','silent']
  prefix = await grab_prefix(ctx) # Get the guild prefix
  if not name: # Check for name argument
    await error(ctx, 'Please specify a name for the collab.')
    return
  if not song: # Check for song argument
    await error(ctx, 'Please specify a song for the collab.')
    return
  if not difficulty: # Check for difficulty argument
    await error(ctx, 'Please specify a difficulty for the collab.')
    return
  if not difficulty in valid_difficulties:
    await error(ctx, 'That is not a valid difficulty.')
    return
  if len(name) > 20:
    await error(ctx, 'You cannot create a collab name with more than 20 characters.')
    return
  for i in name:
    if i not in string.ascii_letters:
      try:
        int(i)
      except:
        await error(ctx, 'That is not a valid name.')
        return
  difficulty = difficulty.capitalize()
  try: # Try statement to handle exception if the song is invalid
    yt = YouTube(song) # Get the song
    songtitle = yt.title
  except: # Catch the exception
    await error(ctx, f'That is not a valid YouTube URL.')
  try:
    database.create(f'{ctx.guild.id}{name}') # Check if a collab exists with that name
  except Exception as err:
    await error(ctx, 'This server already has a collab with that name.')
    print(traceback.format_exc())
  database.connect(f'{ctx.guild.id}{name}') # Connect to the json

  x = { # Dict that will be added to the json
    'host_discord_id': ctx.author.id,
    'name': name,
    'song': {
      'link': song,
      'title': songtitle
    },
    'difficulty': difficulty
  }
  database.dump(f'user_{ctx.author.id}', ctx.author.id)
  database.dump('main_data', x) # Dump the json data
  database.connect_clear() # Clear the connection

  await normalembed(ctx, 'Collab Created!', f'The collab `{name}` has been created.\n**Host:** {ctx.author.mention}\n**Song:** `{songtitle}`\n**Difficulty:** `{difficulty}`') # Send the embed

@client.command()
@commands.has_permissions(administrator=True)
async def invite(ctx, member: discord.Member = None, args = None): # Handles collab invites
  if not args: # If a collab isnt specified
    await error(ctx, 'Please specify a collab.')
    return
  if not member: # If a member isnt specified
    await error(ctx, 'Please specify a member.')
    return

  database = jsondb.Client('database/') # Load the jsondb client
  try:
    database.connect(f'{ctx.guild.id}{args}') # Attempt to connect to the json
  except:
    await error(ctx, 'That collab doesn\'t exist.') # If it fails
    return
  
  try:
    database.load(f'invite_{member.id}') # Load the member invite json
    await error(ctx, 'That user is already invited to this collab!') # If it exists (meaning it won't fail), it means they are already invited
    return
  except: # yeah
    pass
  try:
    database.load(f'user_{member.id}') # Load the user json
    await error(ctx, 'That user is already in this collab!') # If it exists (meaning it won't fail), it means they have already joined
    return
  except: # yeah
    pass

  pre = await grab_prefix(ctx) # Get the guild prefix
  database.dump(f'invite_{member.id}', f'You have joined the collab `{args}`!') # Dump the json
  database.connect_clear() # Clear the connection
  await normalembed(ctx, 'Member Invited!', f'{member.mention} has been invited to the collab `{args}`! They can use `{pre}join "{args}"` to join it!') # Send the embed

@client.command(aliases=['accept'])
async def join(ctx, args = None): # Handles collab joins
  if not args: # If a collab isnt specified
    await error(ctx, 'Please specify a collab.')
    return
  database = jsondb.Client('database/') # Load the jsondb client
  try:
    database.connect(f'{ctx.guild.id}{args}') # Try and connect to the db
  except:
    await error(ctx, 'That collab doesn\'t exist.') # If it doesn't exist
    return
  
  try:
    embed = await customembed(ctx, 'Collab Joined!', database.load(f'invite_{ctx.author.id}')) # Get an embed variable
    host = client.get_user(int(database.load('main_data').get('host_discord_id'))) # Get the host as a member object by loading their id from the main_data json key
    await ctx.send(f'Hey {host.mention}, {ctx.author.mention} has joined your collab!', embed=embed) # Send the message and embed
  except:
    await error(ctx, 'You don\'t have an invite to this collab!') # If they don't have an invite
    return
  database.delete(f'invite_{ctx.author.id}') # Remove the invite
  database.dump(f'users_{ctx.author.id}', ctx.author.id) # Add them to the users
  database.connect_clear() # Clear the connection
  
  

@client.command(aliases=['remove'])
@commands.has_permissions(administrator=True)
async def delete(ctx, args = None): # Handles collab deletions
  database = jsondb.Client('database/') # Load the jsondb client
  if not args: # If a collab isn't specified
    await error(ctx, 'Please specify a collab to remove.')
    return
  try:
    database.remove(f'{ctx.guild.id}{args}') # Try and remove the json file
  except:
    await error(ctx, 'That collab doesn\'t exist.') # If it fails
    return
  await normalembed(ctx, 'Collab Removed!', f'The collab `{args}` has been removed.') # Send the embeds

@client.command(aliases=['add_part'])
@commands.has_permissions(administrator=True)
async def addpart(ctx, member: discord.Member = None, args = None, start = None, end = None, deadline = None):
  database = jsondb.Client('database/') # Load the jsondb client
  if not args: # If a collab isn't specified
    await error(ctx, 'Please specify a collab.')
    return
  if not member: # If a member isn't specified
    await error(ctx, 'Please specify a member.')
    return
  if not deadline: # If a deadline isn't specified
    await error(ctx, 'Please specify a deadline.')
    return
  if not start: # If a start offset isn't specified
    await error(ctx, 'Please specify a start offset.')
    return
  if not end: # If a end offset isn't specified
    await error(ctx, 'Please specify a end offset.')
    return
  try: # Check for a valid deadline
    day,month,year = deadline.split('/') # Split it at a /
    int(day) # Check if they are ints
    int(month)
    int(year)
  except: # Catch the exception
    await error(ctx, 'That is not a valid deadline')
    return
  deadline = day.join('/') + month.join('/') + year.join('/') # Rebuild the deadline variable
  try: # Check for valid offsets
    int(start)
    int(end)
    if start > end:
      0/0 # Cause an error
  except: # Catch the exception
    await error(ctx, 'That is not a valid start/end offset.')
    return

  try:
    database.connect(f'{ctx.guild.id}{args}') # Try and connect to the db
  except:
    await error(ctx, 'That collab doesn\'t exist.') # If it doesn't exist
    return
  try:
    database.load(f'user_{member.id}') # Load the member json
    return
  except: # yeah
    await error(ctx, 'That user is not in this collab.')
  
  x = { # Json that will be put in the database
    'id': member.id, # Member id
    'start': start, # Start offset
    'end': end, # End offset
    'deadline': deadline # Deadline
  }
  database.dump(f'part_{member.id}', x) # Dump the json
  database.connect_clear() # Clear the connection
  embed = await customembed(ctx, 'Part Added!', f'Added a part for {member.mention} from `{start} - {end}`\n**Deadline:** `{deadline}`') # Get the embed
  await ctx.send(member.mention + ", a part was added for you!", embed=embed) # Send the message

@client.command()
async def eval(ctx, *, args):
  if not str(ctx.author.id) == '736038441384542268':
    await error(ctx, 'You cannot run this command.')
    return
  run = args.split('```')

  try:
    async def _eval(ctx):
      exec(run[1])
    
    asyncio.run(_eval(ctx))
  except Exception as err:
    await error(ctx, f'```py\n{traceback.format_exc()}```')

client.run(os.getenv('token')) # Run the bot using token from .env file
