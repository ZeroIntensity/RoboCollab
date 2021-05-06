import discord
from .colors import *
async def customembed(ctx, title=None, msg=None, col=colors.success): # Embed that I can add fields to
  embed=discord.Embed(color=col)
  embed.timestamp=(ctx.message.created_at)
  if not title == None: # If the title argument isn't specified
    embed.title=title
  if not msg == None: # If the msg argument isn't specified
    embed.description=msg
  embed.set_footer(text='RoboCollab')
  embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
  return embed # Returns the embed instead of sending it