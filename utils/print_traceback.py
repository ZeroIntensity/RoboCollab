import traceback as tb

def print_traceback(err):
    tb.print_exception(etype=None, value=err, tb=err.__traceback__)