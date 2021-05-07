# For Windows

import os


path = os.path.abspath(os.path.dirname(__file__)) + '\\'

os.mkdir(path + 'private')
os.mkdir(path + 'private\\database')


f = open(path + 'private\\env.py', 'w+')
f.write('''
import dotenv # Needed to load the .env file
dotenv.load_dotenv() # Load the .env file
import os

class env:
    def __init__(self):
        self.token = os.getenv('token')
        self.password = os.getenv('password')
        self.secret = os.getenv('secret')

''')
f.close()


f = open(path + 'private\\.env', 'w+')
f.write('''
token=bot token here
password=gd password here
secret=bot secret here
''')
f.close()

f = open(path + 'private\\prefixes.json', 'w+')
f.write('{}')
f.close()

f = open(path + 'private\\users.json', 'w+')
f.write('{}')
f.close()

os.system('pip3 install gd.py')
os.system('pip3 install discord.py')
os.system('pip3 install requests')
os.system('pip3 install flask-discord')
os.system('pip3 install gevent')
os.system('pip3 install bs4')
os.system('pip3 install python-dotenv')