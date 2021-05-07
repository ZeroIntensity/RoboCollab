import json
from .get_private_folder import get_private_folder

async def grab_prefix(ctx): # This one is used just to grab the guilds prefix in commands
  with open(f"{get_private_folder()}prefixes.json", "r") as f:
    prefixes = json.load(f) # Load the json
    return prefixes[str(ctx.guild.id)] # Return the prefix
