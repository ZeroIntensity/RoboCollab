from .sql import SQL

def get_collab_sql(rcid): # Function for getting collab sql data

    resp = SQL('get_collab_by_rcid.sql', {"rc_id": rcid}) # Run the SQL query
    collab = resp[0] # Get the response

    return collab # Return the collab