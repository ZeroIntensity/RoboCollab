def color(col): # Function for getting colors
    col = col.lower() # Set the color name to lowercase

    # why does python not have switch statements

    if col == "white":
        return 0xffffff
    
    if col == "black":
        return 0x000000
    
    if col == "orange":
        return 0xff8400
    
    if col == "yellow":
        return 0xffe500
    
    if col == "green":
        return 0x00ff20
    
    if col == "aqua":
        return 0x00eaff
    
    if col == "blue":
        return 0x006dff
    
    if col == "purple":
        return 0x5700ff
    
    if col == "pink":
        return 0xfd00ff
    
    if col == "red":
        return 0xff0004
    
    if col == "light_gray":
        return 0xacacac
    
    if col == "dark_gray":
        return 0x686868
    
    if col == "mint":
        return 0x00ff74
    
    if col == "light_red":
        return 0xff4343
    
    raise ValueError("Invalid color.") # Raise an error if nothing is returned