import discord


async def error(ctx, msg): # Premade embed for invalid arguments
  embed=discord.Embed(color=0xff4444)
  embed.timestamp=(ctx.message.created_at)
  embed.title='Error'
  embed.description=msg # Set the description to the msg argument
  embed.set_footer(text='RoboCollab')
  embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
  await ctx.send(embed=embed) # Send the embed
  return