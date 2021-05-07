import os

def get_private_folder():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '\\private\\'