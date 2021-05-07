import json
from .get_private_folder import get_private_folder
async def get_prefix(client, message): # This one is for the command_prefix
  with open(f"{get_private_folder()}prefixes.json", "r") as f:
    prefixes = json.load(f)
    return prefixes[str(message.guild.id)]
