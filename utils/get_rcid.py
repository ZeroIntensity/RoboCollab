from .sql import SQL

def get_rcid(ctx, name): # Function for getting rcid
    sql = {
            "dc_id": ctx.guild.id,
            "collab_name": name
        }

    resp = SQL('get_rcid.sql', sql) # Run the SQL
    rcid = resp[0][0] # Get the response

    return rcid # Return the rcid