from flask import Blueprint, render_template
from utils import *

basic_pages = Blueprint('basic_pages', __name__, template_folder='./web/html/basic')

@basic_pages.route('/home')
def home():
    return render_template('home.html', head = header('home'))