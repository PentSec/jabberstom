def run_command(msg, *args):
    """Besa a un user

Opcionalmente puede especificar la parte del cuerpo: \
besar <nick> <parte del cuerpo>
    """
    args_len = len(args)
    chat_type = 'groupchat'
    if not args:
        return chat_type, 'A quien debo besar?'
    if args_len == 1:
        return chat_type, '/me Besa a {} :-*'.format(args[0])
    elif args_len == 2:
        return chat_type, '/me Besa a {} y con la lengua en el/la {} :-*'.format(args[0],
                                                               args[1])
    else:
        return chat_type, 'Demasiados argumentos'
