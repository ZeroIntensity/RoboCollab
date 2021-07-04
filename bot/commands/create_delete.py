from discord.ext import commands
import discord
from utils import *

class CreateDelete(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["create"])
    async def createcollab(self, name, song, difficulty):
        vals = self.client.rc_vals

    @createcollab.error
    async def createcollab_err(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            d = {
                "name": "req",
                "song": "req",
                "difficulty": "req"
            }
            await embed(ctx, 'Error', f'Invalid arguments.\n{build_args_help(await grab_prefix(ctx), "createcollab", d)}', color=color("light_red"))
        
        else: 
            await embed(ctx, 'Failure', f'RoboCollab ran into an issue processing your command! \n\n**Error Message**\n```py\n{error}```**Please report this to the developers!**', color = color("red"))
            print(f'Commmand Failure: {print_traceback(error)}')

        
def setup(client):
    client.add_cog(CreateDelete(client))
