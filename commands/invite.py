from discord.ext import commands # Import commands
from utils import *
import jsondb

class Invite(commands.Cog):
    def __init__(self, bot): # For passing in the client
        self.client = bot # Set the client to the client
    
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def invite(self, ctx, member: discord.Member = None, args = None): # Handles collab invites


        database = jsondb.Client('private/database/') # Load the jsondb client
        try:
            database.connect(f'{ctx.guild.id}{args}') # Attempt to connect to the json
        except:
            await error(ctx, 'That collab doesn\'t exist.') # If it fails
            return
        
        try:
            database.load(f'invite_{member.id}') # Load the member invite json
            await error(ctx, 'That user is already invited to this collab!') # If it exists (meaning it won't fail), it means they are already invited
            return
        except: # yeah
            pass
        try:
            database.load(f'user_{member.id}') # Load the user json
            await error(ctx, 'That user is already in this collab!') # If it exists (meaning it won't fail), it means they have already joined
            return
        except: # yeah
            pass

        pre = await grab_prefix(ctx) # Get the guild prefix
        database.dump(f'invite_{member.id}', f'You have joined the collab `{args}`!') # Dump the json
        database.connect_clear() # Clear the connection
        await normalembed(ctx, 'Member Invited!', f'{member.mention} has been invited to the collab `{args}`! They can use `{pre}join "{args}"` to join it!') # Send the embed