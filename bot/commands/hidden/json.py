from discord.ext import commands # Import commands
from utils import *
import discord
import os


class Json(commands.Cog):
    def __init__(self, bot): # For passing in the client
        self.client = bot # Set the client to the client
    
    @commands.command() # totally not stolen yes
    @commands.has_permissions(administrator=True)
    async def json(self, ctx, collab):
        try:
            f = open(f'{get_private_folder()}database\\{ctx.guild.id}{collab}.json')
            json = f.read()
            f.close()
        except:
            await error(ctx, 'This server does not have a collab with that name.')
            return
        
        json = json.replace(', ',',')
        json = json.replace(',',',\n')
        json = json.replace('{','{\n')
        json = json.replace('}','\n}')
        indents = -1
        new = ''
        
        for i in json.split('\n'):
            indent = ''
            for x in range(indents):
                indent += '    '
            
            new += indent + i + '\n'
            if '{' in i:
                indents += 1

            if '}' in i:
                indents -= 1
        json = new
        try:
            await normalembed(ctx, 'Collab JSON',f'Raw JSON of collab `{collab}`\n```yaml\n{json}\n```')
        except:
            f = open(f'{ctx.guild.id}_{collab}_json.json','w')
            f.write(json)
            f.close()
            file = discord.File(f'{ctx.guild.id}_{collab}_json.json')
            await ctx.send('Woah! This JSON file was too big to send on discord, so I have to send it as a JSON file instead!', file=file)
            os.remove(f'{ctx.guild.id}_{collab}_json.json')