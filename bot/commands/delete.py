from discord.ext import commands
import discord
from utils import *
import string
import os
import json

class Delete(commands.Cog): # Cog for delete command
    def __init__(self, client):
        self.client = client


    @commands.command(aliases=["delete"]) # Set an alias to "delete"
    @commands.has_permissions(administrator=True) # Only allow the command to be executed by admins
    async def deletecollab(self, ctx, name):
        vals = self.client.rc_vals
        conf = vals["config"]
        
        if not check_collab_exists(ctx.guild.id, name):
            return await error(ctx, f'`{name}` does not exist.')

        sql = {
            "dc_id": ctx.guild.id,
            "collab_name": name
        }

        resp = SQL('get_rcid.sql', sql)
        rcid = resp[0][0]
        resp = SQL('get_collab_by_rcid.sql', {"rc_id": rcid})
        collab = resp[0]

        SQL('delete_entry.sql', {"rc_id": rcid})
        os.remove(collab[2])

        await success(ctx, f'**Success!** `{name}` has been deleted!') # Send success embed

    @deletecollab.error
    async def createcollab_err(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument): # If an argument is missing
            d = {
                "name": "req"
            } # Data for building args help
            await embed(ctx, 'Error', f'Invalid arguments.\n{build_args_help(await grab_prefix(ctx), "delete", d)}', color=color("light_red")) # Send error
        
        elif isinstance(error, commands.MissingPermissions): # If the user does not have sufficent permissions
            await embed(ctx, 'Error', f'You do not have permission to run this command.', color=color("light_red")) # Send error
        
        else: # If an exception occured
            await embed(ctx, 'Failure', f'RoboCollab ran into an issue processing your command! \n\n**Error Message**\n```py\n{error}```**Please report this to the developers!**', color = color("red"))
            print(f'Commmand Failure: ', end = "") # Print the error
            print_traceback(error)
        

        
def setup(client):
    client.add_cog(Delete(client))
