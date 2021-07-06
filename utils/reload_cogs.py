import os

def reload_cogs(client): # Function for reloading cogs
    reloaded = []
    loaded = []
    for filename in os.listdir('./commands'): # Iterate through commands directory
        if filename.endswith('.py'): # If the file is a python file
            try:
                client.reload_extension(f'commands.{filename[:-3]}') # Reload the extension
                reloaded.append(f'`commands.{filename[:-3]}`')
            except: # If it fails
                client.load_extension(f'commands.{filename[:-3]}') # Load the extension
                loaded.append(f'`commands.{filename[:-3]}')
                    
            msg = "Reloaded "
            for i in reloaded:
                msg += '``' + i + '``, '
            
            msg = msg[:-2] # Remove last comma

            msg += "\nLoaded " # Add loaded section
            for x in loaded:
                msg += '``' + x + '``, '
            msg = msg[:-2] # Remove last comma
            print(msg)

            return msg # Return the message