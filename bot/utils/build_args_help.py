def build_args_help(prefix, command, args):
    resp = f"\n**<>** symbols mean that an argument is **required**.\n**[]** symbols mean that an argument is **optional**.\n\n**Usage**```{prefix}command "
    for i in args:
        if args[i] == 'optional':
            resp += f'[{i}] '
        else:
            resp += f'<{i}> '
    
    return resp + '```'