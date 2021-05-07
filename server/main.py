from flask import Flask, render_template, url_for, request # Import needed things for flask
from flask_discord import DiscordOAuth2Session, requires_authorization, Unauthorized # Import needed things for flask-discord
from gevent.pywsgi import WSGIServer
from private.env import env
import os

ENV = env()

app = Flask(__name__) # Initalize the flask client

app.secret_key = b""
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "true"      # !! Only in development environment.
app.config["DISCORD_CLIENT_ID"] = 754902431258771567   # Discord client ID.
app.config["DISCORD_CLIENT_SECRET"] = ENV.secret                # Discord client secret.
app.config["DISCORD_REDIRECT_URI"] = "https://robocollab.xyz"                 # URL to your callback endpoint.
app.config["DISCORD_BOT_TOKEN"] = ENV.token                    # Required to access BOT resources.

discord = DiscordOAuth2Session(app) # Initalize the flask-discord oauth session
@app.route("/login/")
def login():
    return discord.create_session()




@app.route("/callback/")
def callback():
    discord.callback()
    user = discord.fetch_user()
    welcome_user(user)
    return redirect(url_for(".me"))


@app.route("/me/")
@requires_authorization
def me():
    user = discord.fetch_user()
    return f"""
    <html>
        <head>
            <title>{user.name}</title>
        </head>
        <body>
            <img src='{user.avatar_url}' />
        </body>
    </html>"""

if __name__ == '__main__':
    print('Starting...')
    http_server = WSGIServer(('127.0.0.1', 5000), app) # Initalize the WSGI server
    http_server.serve_forever() # Start the server