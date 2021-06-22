from discord.ext import commands # Import commands
from utils import *
class Join(commands.Cog): # Create the cog subclass
    def __init__(self, bot, jsondb): # For passing in the client
        self.client = bot # Set the client to the client
        self.jsondb = jsondb
    @commands.command(aliases=['accept'])
    async def join(self, ctx, args = None): # Handles collab joins
        if not args: # If a collab isnt specified
            await error(ctx, 'Please specify a collab.')
            return
        database = await self.jsondb.database(f'{get_private_folder()}database\\') # Load the jsondb client
        try:
            json = await database.connect(f'{ctx.guild.id}{args}.json') # Try and connect to the db
        except:
            await error(ctx, 'That collab doesn\'t exist.') # If it doesn't exist
            return
        
        embed = await customembed(ctx, 'Collab Joined!', json[f'invite_{ctx.author.id}']) # Get an embed variable
        host = client.get_user(int(json['main_data'].get('host_discord_id'))) # Get the host as a member object by loading their id from the main_data json key
        await ctx.send(f'Hey {host.mention}, {ctx.author.mention} has joined your collab!', embed=embed) # Send the message and embed
        
        try:
            json.delete(f'invite_{ctx.author.id}') # Remove the invite
        except:
            await error(ctx, 'You don\'t have an invite to this collab!') # If they don't have an invite
            return
        await json.dump(f'users_{ctx.author.id}', None) # Add them to the users
        

