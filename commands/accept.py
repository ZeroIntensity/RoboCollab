from discord.ext import commands
from utils import *
import json
import discord

class Accept(commands.Cog): # Cog for accept command
    def __init__(self, client):
        self.client = client


    @commands.command()
    async def accept(self, ctx, name):
        vals = self.client.rc_vals
        conf = vals["config"] # Load config
        
        if not check_collab_exists(ctx.guild.id, name): # Check if the collab exists
            return await error(ctx, f'`{name}` does not exist.')

        rcid = get_rcid(ctx, name) # Get the rcid
        collab = get_collab_sql(rcid) # Get the collab sql data

        with open(collab[2]) as f:
            load = json.load(f) # Load the json data
        
        try:

            if not load["users"][str(ctx.author.id)] == "inv": # If the user is not invited
                return await error(ctx, f'You are already in the collab `{name}`.') # Send error embed
        except KeyError: # Catch error
            return await error(ctx, f'You do not have an invite to the collab `{name}`.') # Send error embed

        load["users"][str(ctx.author.id)] = "joined"

        with open(collab[2], 'w+') as f:
            json.dump(load, f, indent=4) # Dump json data

        return await success(ctx, f'**Success!** You have joined the collab `{name}`!')


    @accept.error
    async def err(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument): # If an argument is missing
            d = {
                "name": "req",
                "user": "req"
            } # Data for building args help
            await embed(ctx, 'Error', f'Invalid arguments.\n{build_args_help(await grab_prefix(ctx), "delete", d)}', color=color("light_red")) # Send error

        elif isinstance(error, commands.MissingPermissions): # If the user does not have sufficent permissions
            await embed(ctx, 'Error', f'You do not have permission to run this command.', color=color("light_red")) # Send error
        
        else: # If an exception occured
            await embed(ctx, 'Failure', f'RoboCollab ran into an issue processing your command! \n\n**Error Message**\n```py\n{error}```**Please report this to the developers!**', color = color("red"))
            print(f'Commmand Failure: ', end = "") # Print the error
            print_traceback(error)
        

        
def setup(client):
    client.add_cog(Accept(client))
