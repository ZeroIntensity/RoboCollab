from discord.ext import commands
from utils import *
import json
import discord

class Invite(commands.Cog): # Cog for invite command
    def __init__(self, client):
        self.client = client


    @commands.command()
    @commands.has_permissions(administrator=True) # Only allow the command to be executed by admins
    async def invite(self, ctx, name, user: discord.Member):
        vals = self.client.rc_vals
        conf = vals["config"] # Load config
        
        if not check_collab_exists(ctx.guild.id, name): # Check if the collab exists
            return await error(ctx, f'`{name}` does not exist.')

        rcid = get_rcid(ctx, name) # Get the rcid
        collab = get_collab_sql(rcid) # Get the collab sql data
        with open(collab[2]) as f:
            load = json.load(f) # Load the json data
        
        try:
            load["users"][str(user.id)] # Check if the user is already invited or joined the collab
            return await error(ctx, f'`{user}` has already been invited to or joined this collab.') # Send error embed
        except KeyError: # Catch error
            pass
            
        load["users"][str(user.id)] = "inv" # Add invite to json

        with open(collab[2], 'w+') as f:
            json.dump(load, f, indent=4) # Dump json data

        pre = await grab_prefix(ctx) # Grab the guild's prefix

        await success(ctx, f'**Success!** `{user}` has been invited to the collab `{name}`!\nThey can use `{pre}accept "{name}"` to join!') # Send success embed

    @invite.error
    async def err(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument): # If an argument is missing
            d = {
                "name": "req",
                "user": "req"
            } # Data for building args help
            await embed(ctx, 'Error', f'Invalid arguments.\n{build_args_help(await grab_prefix(ctx), "delete", d)}', color=color("light_red")) # Send error
        
        elif isinstance(error, commands.MemberNotFound): # If the member is not found
            await embed(ctx, 'Error', f'Invalid member.\n', color=color("light_red")) # Send error

        elif isinstance(error, commands.MissingPermissions): # If the user does not have sufficent permissions
            await embed(ctx, 'Error', f'You do not have permission to run this command.', color=color("light_red")) # Send error
        
        else: # If an exception occured
            await embed(ctx, 'Failure', f'RoboCollab ran into an issue processing your command! \n\n**Error Message**\n```py\n{error}```**Please report this to the developers!**', color = color("red"))
            print(f'Commmand Failure: ', end = "") # Print the error
            print_traceback(error)
        

        
def setup(client):
    client.add_cog(Invite(client))
