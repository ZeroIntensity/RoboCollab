from discord.ext import commands # Import commands
from utils import *
import jsondb
class Join(commands.Cog): # Create the cog subclass
    def __init__(self, bot, jsondb): # For passing in the client
        self.client = bot # Set the client to the client
        self.jsondb = jsondb
    @commands.command(aliases=['part_list'])
    async def partlisst(self, ctx, collab = None): # Handles collab joins
        if not collab: # If a collab isnt specified
            await error(ctx, 'Please specify a collab.')
            return
        database = self.jsondb.Client(f'{get_private_folder()}database/') # Load the jsondb client
        try:
            database.connect(f'{ctx.guild.id}{args}') # Try and connect to the db
        except:
            await error(ctx, 'That collab doesn\'t exist.') # If it doesn't exist
            return
        
        try:
            embed = await customembed(ctx, 'Collab Joined!', database.load(f'invite_{ctx.author.id}')) # Get an embed variable
            host = client.get_user(int(database.load('main_data').get('host_discord_id'))) # Get the host as a member object by loading their id from the main_data json key
            await ctx.send(f'Hey {host.mention}, {ctx.author.mention} has joined your collab!', embed=embed) # Send the message and embed
        except:
            await error(ctx, 'You don\'t have an invite to this collab!') # If they don't have an invite
            return
        database.delete(f'invite_{ctx.author.id}') # Remove the invite
        
        database.connect_clear() # Clear the connection
        

