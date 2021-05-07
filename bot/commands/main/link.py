import json
from discord.ext import commands

class Link(commands.Cog):
    def __init__(self, bot, gmd): # For passing in the client
        self.client = bot # Set the client to the client
        self.gmd = gmd
    

    @commands.command() # Define a bot command
    async def link(self, ctx, *, args = None): # Account linking command
        gmd = self.gmd
        if not args:
            await error('Please specify an account')
            return
        try:
            user = await gmd.find_user(args) # Check to see if the user exists
        except gd.MissingAccess:
            await error('That account doesn\'t exist')
            return
        with open("private/users.json", "r") as f:
            users = json.load(f)
        x = { # Dict that will be added to the json
            'linktype': 'unverified',
            'account_id': user.account_id
        }
        users[int(ctx.author.id)] = x

        with open("private/users.json", "w") as f:
            json.dump(users, f) # Dump the json data
        
        await normalembed(ctx, 'Account Link',f'Waiting to link `{args}`. Please message **"verify"** to the account **RoboCollab** on GD.')