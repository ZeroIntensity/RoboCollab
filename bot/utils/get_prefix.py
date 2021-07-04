import json

async def get_prefix(client, message): # This one is for the command_prefix
  with open(f"private/prefixes.json", "r") as f:
    prefixes = json.load(f)
    return prefixes[str(message.guild.id)]
