from wikipedia import wikipedia

def run_command(msg, *args):
    """Busqueda en wikipedia"""
    mtype = 'groupchat'
    if args:
        sh = wikipedia.summary(args)
        return mtype, 'Hello'
    return mtype, 'que debo buscar?'
