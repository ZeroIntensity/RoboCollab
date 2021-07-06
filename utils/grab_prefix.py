import json

async def grab_prefix(ctx): # This one is for the command_prefix
  with open(f"private/prefixes.json", "r") as f:
    prefixes = json.load(f)
    return prefixes[str(ctx.guild.id)]
