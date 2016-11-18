def run_command(msg, *args):
    """Abrazar a un user"""
    mtype = 'groupchat'
    if args:
        return mtype, '/me Abraza a {}'.format(' '.join(args))
    return mtype, 'A quien debo dar el abracito?'
