from discord.ext import commands # Import commands
from utils import *

class Delete(commands.Cog):
    def __init__(self, bot): # For passing in the client
        self.client = bot # Set the client to the client

    @commands.command(aliases=['remove'])
    @commands.has_permissions(administrator=True)
    async def delete(self, ctx, args = None): # Handles collab deletions
        database = jsondb.Client('private/database/') # Load the jsondb client
        if not args: # If a collab isn't specified
            await error(ctx, 'Please specify a collab to remove.')
            return
        try:
            database.remove(f'{ctx.guild.id}{args}') # Try and remove the json file
        except:
            await error(ctx, 'That collab doesn\'t exist.') # If it fails
            return
        await normalembed(ctx, 'Collab Removed!', f'The collab `{args}` has been removed.') # Send the embeds
