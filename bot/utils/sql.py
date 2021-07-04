import sqlite3
from pathlib import Path
import os
from .resolve_top import resolve_top

def SQL(file, vals = None): # Function for running SQL queries
    top = resolve_top() # Get top folder

    db = Path(os.path.join(top, 'private\\database\\main.db')) # Get the database
    conn = sqlite3.connect(db) # Connect to database
    cursor = conn.cursor() # Get cursor
    with open(os.path.join(top, f"sql\\{file}")) as f:
        lines = f.read() # Read the SQL file
    if vals:
        for i in vals:
            lines = lines.replace("{" + i + "}", vals[i]) # Insert vals

    for line in lines.split(';'): # Iterate through each command
        if line == "":
            break
        cursor.execute(line) # Execute the command
    resp = cursor.fetchall()

    conn.commit() # Commit the changes
    conn.close() # Close the connection

    return resp

