def run_command(msg, *args):
    """Saluda a un user :D!"""
    mtype = 'groupchat'
    if args:
        return mtype, 'Hola {} Bienvenido a la Sala de SecHackLabs, Pregunta lo que quieras seguro alguien te respondera, Te invitamos a leer las reglas de esta sala escribiendo !regla'.format(' '.join(args))
    return mtype, ' Bienvenidos a la Sala de SecHackLabs, Pregunta lo que quieras seguro alguien te respondera, Te invitamos a leer las reglas de esta sala escribiendo !regla'
