from discord.ext import commands
from utils import *
import os
import discord

class Debug(commands.Cog): # Cog for debug command
    def __init__(self, client):
        self.client = client


    @commands.command()
    @commands.has_permissions(administrator=True) # Only allow the command to be executed by admins
    async def debug(self, ctx, operation, *, args = None):
        vals = self.client.rc_vals
        conf = vals["config"] # Load config
        if not check_rc_perms(ctx.author.id, 'developer', conf): # Check if user is a developer
            return await error(ctx, 'This is a developer only command.')
        
        if (operation == "sql_read_all") or (operation == "allsql"):
            try:
                resp = SQL('get_all_data.sql') # Get all SQL data
                if len(resp) > 2000: # If it's above 2000 characters
                    with open('./private/temp/sql_data.temp', 'w+') as f:
                        f.write(resp) # Write temp file
                    
                    await ctx.author.send('Unfortunately, the SQL data is above 2000 characters, so I have to send it as a file instead.', file = discord.File('./private/temp/sql_data.temp')) # Send messsage
                    os.remove('./private/temp/sql_data.temp') # Remove temporary file
                else:
                    await ctx.author.send(f'```py\n{resp}\n```') # Send messsage
                return await success(ctx, f'{ctx.author.mention}, check your DM\'s!')
            except:
                return await error(ctx, 'I cannot run this command as your DM\'s are not open.') # If it fails
        else:
            return await error(ctx, 'That is not a valid operation.') # If the operation is invalid
        

    @debug.error
    async def err(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument): # If an argument is missing
            d = {
                "operation": "req"
            } # Data for building args help
            await embed(ctx, 'Error', f'Invalid arguments.\n{build_args_help(await grab_prefix(ctx), "delete", d)}', color=color("light_red")) # Send error
        
        elif isinstance(error, commands.MissingPermissions): # If the user does not have sufficent permissions
            await embed(ctx, 'Error', f'You do not have permission to run this command.', color=color("light_red")) # Send error
        
        else: # If an exception occured
            await embed(ctx, 'Failure', f'RoboCollab ran into an issue processing your command! \n\n**Error Message**\n```py\n{error}```**Please report this to the developers!**', color = color("red"))
            print(f'Commmand Failure: ', end = "") # Print the error
            print_traceback(error)
        

        
def setup(client):
    client.add_cog(Debug(client))
