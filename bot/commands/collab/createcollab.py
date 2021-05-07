from discord.ext import commands # Import commands
from utils import *
import jsondb
import string
import requests
from bs4 import BeautifulSoup
import traceback
class CreateCollab(commands.Cog): # Create the cog subclass
    def __init__(self, bot, jsondb): # For passing in the client
        self.client = bot # Set the client to the client
        self.jsondb = jsondb
    @commands.command(aliases=['create','cc','create_collab'])
    @commands.has_permissions(administrator=True)
    async def createcollab(self, ctx, name = None, song = None, difficulty = None):
        database = self.jsondb.Client(f'{get_private_folder()}database/')
        valid_difficulties = ['auto','easy','normal','hard','harder','insane','easy demon','medium demon','hard demon','insane demon','extreme demon','silent'] # All the valid difficulties
        prefix = await grab_prefix(ctx) # Get the guild prefix
        if not name: # Check for name argument
            await error(ctx, 'Please specify a name for the collab.')
            return
        if not song: # Check for song argument
            await error(ctx, 'Please specify a song for the collab.')
            return
        if not difficulty: # Check for difficulty argument
            await error(ctx, 'Please specify a difficulty for the collab.')
            return
        if not difficulty in valid_difficulties:
            await error(ctx, 'That is not a valid difficulty.')
            return
        if len(name) > 20:
            await error(ctx, 'You cannot create a collab name with more than 20 characters.')
            return
        for i in name:
            if i not in string.ascii_letters:
              try:
                  int(i)
              except:
                  await error(ctx, 'That is not a valid name.')
                  return
        difficulty = difficulty.capitalize()
        try: # Try statement to handle exception if the song is invalid
            if (not song.startswith('https://youtube.com')) and (not song.startswith('https://www.youtube.com')) and (not song.startswith('https://youtu.be')):
                0/0 # Cause an exception
            resp = requests.get(song)
            soup = BeautifulSoup(resp.text, 'html.parser')
            for titl in soup.find_all('title'):
                title = titl.get_text()
            
            title = title[:-10]
        except Exception as err: # Catch the exception
            await error(ctx, f'That is not a valid YouTube URL. {err}')
            return
        try:
            database.create(f'{ctx.guild.id}{name}') # Check if a collab exists with that name
        except Exception as err:
            await error(ctx, 'This server already has a collab with that name.')
            return
        database.connect(f'{ctx.guild.id}{name}') # Connect to the json

        x = { # Dict that will be added to the json
            'host_discord_id': ctx.author.id,
            'name': name,
            'song': {
                'link': song,
                'title': title
            },
            'difficulty': difficulty
        }
        database.dump(f'user_{ctx.author.id}', ctx.author.id)
        database.dump('main_data', x) # Dump the json data
        database.connect_clear() # Clear the connection

        await normalembed(ctx, 'Collab Created!', f'The collab `{name}` has been created.\n**Host:** {ctx.author.mention}\n**Song:** `{title}`\n**Difficulty:** `{difficulty}`') # Send the embed