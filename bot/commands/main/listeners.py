from discord.ext import commands # Import commands
from utils import *
from discord.ext import tasks # Import commands
import asyncio
import os
import gd

class Listeners(commands.Cog):
    def __init__(self, bot, gmd, env, startingprefix): # For passing in the client
        self.client = bot # Set the client to the client
        self.gmd = gmd
        self.env = env
        self.startingprefix = startingprefix
    @commands.Cog.listener() # Listen for a bot event
    async def on_guild_join(self, guild): # Do when the bot joins a guild
        startingprefix = self.startingprefix
        with open(f"{get_private_folder()}prefixes.json", "r") as f:
            prefixes = json.load(f) # Load the prefixes

        prefixes[int(guild.id)] = startingprefix # Sets the default prefix to '//'

        with open(f"{get_private_folder()}prefixes.json", "w") as f:
            json.dump(prefixes, f) # Dump the json data



    @tasks.loop(seconds=10) # Async task that runs every 10 seconds
    async def autostatus(self):
        client = self.client
        startingprefix = self.startingprefix
        await asyncio.sleep(10) # Waits 10 seconds to switch statuses
        await client.change_presence(activity=discord.Activity(name=f'{len(client.users)} Users! | {startingprefix}prefix <your new prefix>', type=discord.ActivityType.listening))

        await asyncio.sleep(10) # Also waits 10 seconds
        await client.change_presence(activity=discord.Activity(name=f'{len(client.guilds)} Servers! | {startingprefix}help', type=discord.ActivityType.listening))
        await asyncio.sleep(10) # Again, waits 10 seconds
        await client.change_presence(activity=discord.Activity(name=f'https://robocollab.xyz | {startingprefix}help', type=discord.ActivityType.playing))

    @commands.Cog.listener() # Listen for a bot event
    async def on_ready(self):
        startingprefix = self.startingprefix
        gmd = self.gmd
        client = self.client
        env = self.env
        await gmd.login('RoboCollab', env.password) # Logs into GD
        await client.wait_until_ready() # Wait until the bot has logged in
        gd.events.enable(client.loop) # Enable the message listener
        print(f"Logged in as {client.user} ({client.user.id})") # Prints bot tag and ID
        await client.change_presence(activity=discord.Activity(name=f"{len(client.guilds)} Servers! | {startingprefix}help", type=discord.ActivityType.listening))
        self.autostatus.start() # Starts the autostatus
    '''
    @commands.Cog.listener()
    async def on_command_error(self, ctx, err):
        await error(ctx, f'{err}.')
    '''