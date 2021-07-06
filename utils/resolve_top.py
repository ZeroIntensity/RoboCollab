from pathlib import Path

def resolve_top(): # Function for getting top level folder
    top = Path() \
        .resolve()
    
    return top