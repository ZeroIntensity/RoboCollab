from discord.ext import commands
import discord

class OnReady(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        vals = self.client.rc_vals
        starting_prefix = vals.get('config') \
            .get('starting_prefix') # Get starting prefix

        await self.client.wait_until_ready() # Wait until the bot has logged in
        print(f"Logged in as {self.client.user} ({self.client.user.id})") # Prints bot tag and ID
        await self.client.change_presence(activity=discord.Activity(name=f"{len(self.client.guilds)} Servers! | {starting_prefix}help", type=discord.ActivityType.listening)) # Set bot status


def setup(client):
    client.add_cog(OnReady(client))
