from discord.ext import commands # Import commands
from utils import *
from platform import python_version # For python version

class Info(commands.Cog):
    def __init__(self, bot, version): # For passing in the client
        self.client = bot # Set the client to the client
        self.version = version
    @commands.command()
    async def info(self, ctx): # Handles collab invites
        await normalembed(ctx, 'RoboCollab Info', f'''**Language:** `Python {python_version()}`
        **RoboCollab Version:** `V7 {self.version}`
        **Servers:** `{len(self.client.guilds)}`
        **Users:** `{len(self.client.users)}`
        
        **Created by [ZeroIntensity](https://zintensity.net)**
        **RoboCollab's [GitHub](https://github.com/ZeroIntensity/RoboCollab)**''')
