from discord.ext import commands # Import commands
from utils import *
import jsondb
import json
class AddPart(commands.Cog): # Create the cog subclass
    def __init__(self, bot, jsondb): # For passing in the client
        self.client = bot # Set the client to the client
        self.jsondb = jsondb
    @commands.command(aliases=['add_part'])
    @commands.has_permissions(administrator=True)
    async def addpart(self, ctx, collab = None, member: discord.Member = None, start = None, end = None, deadline = None):
        database = self.jsondb.Client(f'{get_private_folder()}database\\') # Load the jsondb client
        
        if not member:
            await error(ctx, 'Please specify a member.')
            return
        if not collab:
            await error(ctx, 'Please specify a collab.')
            return
        if not start:
            await error(ctx, 'Please specify a start offset.')
            return
        if not end:
            await error(ctx, 'Please specify a end offset.')
            return

        if not deadline:
            await error(ctx, 'Please specify a deadline.')
            return

        try: # Check for a valid deadline
            day,month,year = deadline.split('/') # Split it at a /
            int(day) # Check if they are ints
            int(month)
            int(year)
        except Exception as err: # Catch the exception
            await error(ctx, f'That is not a valid deadline.')
            return
        try: # Check for valid offsets
            int(start)
            int(end)
            if start > end:
                0/0 # Cause an error
        except: # Catch the exception
            await error(ctx, 'That is not a valid start/end offset.')
            return
        if int(start) < 0:
            await error(ctx, 'That is not a valid start offset.')
            return

        try:
            jsn = await database.connect(f'{ctx.guild.id}{collab}', create = False) # Try and connect to the db
        except:
            await error(ctx, 'That collab doesn\'t exist.') # If it doesn't exist
            return
        f = open(database.get_conn(None))
        read = f.read()
        f.close()
        for i in json.loads(read):
            if i.startswith('part_'):
                try:
                    if (int(json.loads(read).get(i).get('start')) < int(start)) and (int(json.loads(read).get(i).get('end')) > int(end)):
                        await error(ctx, f'This part would overwrite an existing part. Please remove the existing part before creating a new one via the `{await grab_prefix(ctx)}removepart` command.')
                        return
                except:
                    pass
        try:
            await jsn[f'user_{member.id}'] # Load the member json
        except: # yeah
            await error(ctx, 'That user is not in this collab.')
        
        x = { # Json that will be put in the private/database
            'id': member.id, # Member id
            'start': start, # Start offset
            'end': end, # End offset
            'deadline': deadline # Deadline
        }
        parts = []
        partamount = 0
        for i in json.loads(read):
                if i.startswith(f'part_{member.id}_'):
                    parts.append(int(i[-1]))
        if parts == []: 
            partamount = 1
        else:
            partamount = max(parts)
            partamount += 1
        await jsn.dump(f'part_{member.id}_{partamount}', x) # Dump the json
        embed = await customembed(ctx, 'Part Added!', f'Added a part for {member.mention} from `{start} - {end}`\n**Deadline:** `{deadline}`') # Get the embed
        await ctx.send(member.mention + ", a part was added for you!", embed=embed) # Send the message//json 