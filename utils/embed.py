import discord

async def embed(ctx, title = None, body = None, fields = None, footer = None, color = None, msg = None):
    embed = discord.Embed(color=color) # Initializes the embed

    embed.timestamp = (ctx.message.created_at) # Set the timestamp
    if title: # If title was specified
        embed.title = title # Set the title
    if body: # If body was specified
        embed.description = body # Set the description
    if footer: # If footer was specified
        embed.set_footer(text=footer) # Set the footer
    else:
        embed.set_footer(text="RoboCollab")
    
    embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url) # Set the author
    if msg:
        await ctx.send(msg, embed=embed)
    else:
        await ctx.send(embed=embed)