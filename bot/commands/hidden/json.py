from discord.ext import commands # Import commands
from utils import *
import discord
import os


class Json(commands.Cog):
    def __init__(self, bot, jsondb): # For passing in the client
        self.client = bot # Set the client to the client
        self.jsondb = jsondb
    @commands.command() # totally not stolen yes
    @commands.has_permissions(administrator=True)
    async def json(self, ctx, collab):
        try:
            database = await self.jsondb.database(f'{get_private_folder()}database')
            json = await database.connect(f'{ctx.guild.id}{collab}.json', create=False)
        except:
            await error(ctx, 'This server does not have a collab with that name.')
            return
        
        read = await json.read()
        try:
            await normalembed(ctx, 'Collab JSON',f'Raw JSON of collab `{collab}`\n```yaml\n{json}\n```')
        except:
            f = open(f'{ctx.guild.id}_{collab}_json.json','w')
            f.write(read)
            f.close()
            file = discord.File(f'{ctx.guild.id}_{collab}.json')
            await ctx.send('Woah! This JSON file was too big to send on discord, so I have to send it as a JSON file instead!', file=file)
            os.remove(f'{ctx.guild.id}_{collab}.json')