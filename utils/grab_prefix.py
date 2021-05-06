import json

async def grab_prefix(ctx): # This one is used just to grab the guilds prefix in commands
  with open("private/prefixes.json", "r") as f:
    prefixes = json.load(f) # Load the json
    return prefixes[str(ctx.guild.id)] # Return the prefix
