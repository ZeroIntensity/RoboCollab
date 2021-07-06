from discord.ext import commands
import discord
from utils import *

class Extension(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def extension(self, ctx, operation, extension = None):
            CONFIG = self.client.vals["config"]
            if check_rc_perms(ctx.author.id, "developer", CONFIG): # Check if they have needed perms
                if operation == "reload_all":
                    msg = reload_cogs()
                    return await ctx.send(msg)
                            

                if operation == "load": # If the operation is load
                    self.client.load_extension(f'commands.{extension}') # Load the extension
                    msg = f'`{extension}` was successfully loaded.' # Define the message to be sent
                    print(msg)
                    return await ctx.send(msg) # End the command

                elif operation == "unload": # If the operation is unload
                    self.client.unload_extension(f'commands.{extension}') # Unload the extension
                    msg = f'`{extension}` was successfully unloaded.' # Define the message to be sent
                    print(msg) 
                    return await ctx.send(msg) # End the command

                elif operation == "reload": # If the operation is reload
                    self.client.reload_extension(f'commands.{extension}') # Reload the extension
                    msg = f'`{extension}` was successfully reloaded.' # Define the message to be sent
                    print(msg)
                    return await ctx.send(msg) # End the command



def setup(client):
    client.add_cog(Extension(client))
