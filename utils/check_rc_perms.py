def check_rc_perms(id, needed, config):
    perm_list = config.get('rc_perms') # Get perms list from config
    perms = config.get('perms') # Get perms dict from config
    if not needed in perm_list: # If the needed is not found
        raise ValueError("Invalid permission specified.") # Raise a ValueError
    
    for i in perms: # Iterate through the perms
        if int(perms[i]["discord_id"]) == int(id): # If the ID matches
            if perm_list.index(perms[i]["state"]) >= perm_list.index(needed): # If the index of the current state is higher or equal to the needed permission level, return true
                return True
    
    return False # Finally, return false