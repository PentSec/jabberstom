import os
import random


def run_command(msg, *args):
    """Tu macre es tan .. xD"""
    dirpath = os.path.dirname(os.path.realpath(__file__))
    filepath = os.path.join(dirpath, 'mother_jokes.txt')
    with open(filepath) as f:
        jokes = [joke.strip() for joke in f]
    joke = random.choice(jokes)
    nick = "{}'s".format(' '.join(args)) if args else 'Edu4rd'
    return 'groupchat', joke.format(nick=nick)
