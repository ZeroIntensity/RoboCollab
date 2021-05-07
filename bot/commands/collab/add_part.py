from discord.ext import commands # Import commands
from utils import *
import jsondb
class AddPart(commands.Cog): # Create the cog subclass
    def __init__(self, bot, jsondb): # For passing in the client
        self.client = bot # Set the client to the client
        self.jsondb = jsondb
    @commands.command(aliases=['add_part'])
    @commands.has_permissions(administrator=True)
    async def addpart(self, ctx, member: discord.Member = None, args = None, start = None, end = None, deadline = None):
        database = self.jsondb.Client(f'{get_private_folder()}database/') # Load the jsondb client
        try: # Check for a valid deadline
            day,month,year = deadline.split('/') # Split it at a /
            int(day) # Check if they are ints
            int(month)
            int(year)
        except: # Catch the exception
            await error(ctx, 'That is not a valid deadline')
            return
        deadline = day.join('/') + month.join('/') + year.join('/') # Rebuild the deadline variable
        try: # Check for valid offsets
            int(start)
            int(end)
            if start > end:
                0/0 # Cause an error
        except: # Catch the exception
            await error(ctx, 'That is not a valid start/end offset.')
            return

        try:
            database.connect(f'{ctx.guild.id}{args}') # Try and connect to the db
        except:
            await error(ctx, 'That collab doesn\'t exist.') # If it doesn't exist
            return
        try:
            database.load(f'user_{member.id}') # Load the member json
            return
        except: # yeah
            await error(ctx, 'That user is not in this collab.')
        
        x = { # Json that will be put in the private/database
            'id': member.id, # Member id
            'start': start, # Start offset
            'end': end, # End offset
            'deadline': deadline # Deadline
        }
        database.dump(f'part_{member.id}', x) # Dump the json
        database.connect_clear() # Clear the connection
        embed = await customembed(ctx, 'Part Added!', f'Added a part for {member.mention} from `{start} - {end}`\n**Deadline:** `{deadline}`') # Get the embed
        await ctx.send(member.mention + ", a part was added for you!", embed=embed) # Send the message