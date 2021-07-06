from discord.ext import commands
from utils import *
import string
import os
import json

class Create(commands.Cog): # Cog for create command
    def __init__(self, client):
        self.client = client


    @commands.command(aliases=["create"]) # Set an alias to "create"
    @commands.has_permissions(administrator=True) # Only allow the command to be executed by admins
    async def createcollab(self, ctx, name, song, difficulty):
        vals = self.client.rc_vals
        conf = vals["config"]

        if len(name) > 20: # Check if the name is more than 20 characters
            return await error(ctx, 'Collab names cannot exceed 20 characters.') # Send error embed

        for i in name:
            if i not in string.ascii_letters:
                return await error(ctx, 'That is not a valid collab name.') # Send error embed
        
        if difficulty not in conf["valid_difficulties"]:
            return await error(ctx, f'`{difficulty}` is not a valid difficulty.') # Send error embed
        
        json_path = f'./private/database/json/{name}_{ctx.guild.id}.json' # Generate JSON path
        if os.path.exists(json_path): # Check if the path exists
            return await error(ctx, f'`{name}` is an already existing collab in this server.') # Send error embed
        
        with open(json_path, 'w+') as f: # Create the JSON file
            f.write('{}') # Write the starting text
        with open(json_path) as f:
            load = json.load(f) # Load the JSON
        
        load["host"] = ctx.author.id # Set the host to the author id
        load["name"] = name # Set the name
        load["song"] = song # Set the song
        load["difficulty"] = difficulty # Set the difficulty
        load["guild"] = ctx.guild.id # Set the guild to the guild id
        load["parts"] = {} # Create an empty parts dict
        load["deadlines"] = {} # Create an empty deadlines dict
        load["users"] = {} # Create an empty users dict
        load["roles"] = ["layout", "decoration", "playtester", "merger", "verifier", "host"] # List representing all roles


        with open(json_path, 'w+') as f:
            json.dump(load, f, indent=4) # Dump the JSON data
        
        sql = {
            "dc_id": ctx.guild.id,
            "json_path": json_path,
            "collab_name": name
        } # Dict to process SQL variables


        SQL('add_to_table.sql', sql)
        await success(ctx, f'**Success!** `{name}` has been created!') # Send success embed

    @createcollab.error
    async def err(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument): # If an argument is missing
            d = {
                "name": "req",
                "song": "req",
                "difficulty": "req"
            } # Data for building args help
            await embed(ctx, 'Error', f'Invalid arguments.\n{build_args_help(await grab_prefix(ctx), "createcollab", d)}', color=color("light_red")) # Send error
        
        elif isinstance(error, commands.MissingPermissions): # If the user does not have sufficent permissions
            await embed(ctx, 'Error', f'You do not have permission to run this command.', color=color("light_red")) # Send error
        
        else: # If an exception occured
            await embed(ctx, 'Failure', f'RoboCollab ran into an issue processing your command! \n\n**Error Message**\n```py\n{error}```**Please report this to the developers!**', color = color("red"))
            print(f'Commmand Failure: ', end = "") # Print the error
            print_traceback(error)
        

        
def setup(client):
    client.add_cog(Create(client))
