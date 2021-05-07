from discord.ext import commands # Import commands
from utils import *

class Help(commands.Cog):
    def __init__(self, bot): # For passing in the client
        self.client = bot # Set the client to the client
    
    @commands.command()
    async def help(self, ctx, args = None): # Handles collab invites
        prefix = await grab_prefix(ctx) # Get the guild prefix
        if args:
            args = args.lower()
            if args.lower() == 'main': # Check for main argument
                embed = await customembed(ctx, 'Help', f'**Main Commands**\nUse `{prefix}help <command>` for more help on a command.')
                embed.add_field(name="Ping", value=f"``{prefix}ping``")
                await ctx.send(embed=embed)
                return
        else:

            embed = await customembed(ctx, 'Help', 'Please select a category') # Sent if no/invalid argument is specified
            embed.add_field(name="Main Commands", value=f"``{prefix}help main``")
            embed.add_field(name="GD Commands", value=f"``{prefix}help gd``")
            embed.add_field(name="Collab Commands", value=f"``{prefix}help collab``")
            await ctx.send(embed=embed)