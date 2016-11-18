import os
import random


def run_command(msg, *args):
    """Pegale a un user.

Simplemente: !pegar <nick> 
    """
    nick = ' '.join(args)
    if not nick:
        return 'groupchat', 'Tu tienes que darme un nick'
    dirpath = os.path.dirname(os.path.realpath(__file__))
    filepath = os.path.join(dirpath, 'slaps.txt')
    with open(filepath) as f:
        slaps = tuple(slap.strip() for slap in f)
        slap = random.choice(slaps).format(nick=nick)
        return 'groupchat', '/me {}'.format(slap)
