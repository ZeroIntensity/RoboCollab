import traceback as tb

def print_traceback(err):
    tb.print_traceback(etype=None, value=err, tb=err.__traceback__)