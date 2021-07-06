from private import env
from flask import Flask, render_template, Blueprint
from threading import Thread
import logging
import os
from utils import *
from blueprints import *

os.environ["WERKZEUG_RUN_MAIN"] = "true"
CONFIG = get_server_config() # Get server config

# template_folder=CONFIG["html_path"], static_folder=CONFIG["static_path"]

app = Flask(__name__) # Initalize flask client
log = logging.getLogger('werkzeug') # Get flask logger
# Disable logging
log.disabled = True
app.logger.disabled = True





app.register_blueprint(basic_pages, url_prefix='/')

def run():
    app.run(CONFIG["ip"], int(CONFIG["port"]))

def start():
    server = Thread(target=run)
    server.start()