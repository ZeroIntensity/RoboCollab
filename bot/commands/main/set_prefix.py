from discord.ext import commands # Import commands
from utils import *
class Set_Prefix(commands.Cog):
    def __init__(self, bot): # For passing in the client
        self.client = bot # Set the client to the client
    
    @commands.command(aliases=['prefix']) # Define a bot command
    @commands.has_permissions(manage_guild=True)
    async def setprefix(self, ctx, *, args=None): # Command that changes the guild prefix
        if not args:
            await error(ctx, 'You need to specify a prefix.')
            return
        pre = await grab_prefix(ctx)
        if pre == args: # Checks if its the same as the current prefix
            await error(ctx, 'That is already set as your prefix')
            return
        with open("private/prefixes.json", "r") as f: # Load the prefixes
            prefixes = json.load(f)
            prefixes [str(ctx.guild.id)] = args # Sets the new prefix
        with open("private/prefixes.json", "w") as f:
            json.dump(prefixes, f)
        await normalembed(ctx, 'Set Prefix', f'Set the prefix to `{args}`')