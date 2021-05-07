import os

from discord.ext import commands # Import commands
from utils import *

class Collabs(commands.Cog):
    def __init__(self, bot): # For passing in the client
        self.client = bot # Set the client to the client

    @commands.command(aliases=['collab_list'])
    @commands.has_permissions(administrator=True)
    async def collabs(self, ctx, args = None): # Handles collab deletions
        collabs = []
        for file in os.listdir(f"{get_private_folder()}database"):
            if file.startswith(str(ctx.guild.id)):
                f = file.replace(str(ctx.guild.id), '')
                f = f.replace('.json', '')
                collabs.append(f)
        
        if len(collabs) == 0:
            await normalembed(ctx, 'Collab List', f'This server doesn\'t have any collabs, use ``{await grab_prefix(ctx)}createcollab`` to create one.')
            return

        embed = await customembed(ctx, 'Collab List', f'This server has **{len(collabs)}** collab(s). To remove collabs, use ``{await grab_prefix(ctx)}delete "<collab name>"`` to delete one.')
        for i in collabs:
            embed.add_field(name=i, value=f'``{await grab_prefix(ctx)}data "{i}"``')
        await ctx.send(embed=embed)