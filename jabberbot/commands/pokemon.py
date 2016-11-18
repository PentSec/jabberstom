import os
import random


def run_command(msg, *args):
    """encuentra un salvaje pokemon!"""
    dirpath = os.path.dirname(os.path.realpath(__file__))
    filepath = os.path.join(dirpath, 'pokemon.txt')
    with open(filepath) as f:
        pokeymans = [poke.strip() for poke in f]
        return 'groupchat', 'Un Salvaje ' + random.choice(pokeymans) + ' Aparecio !!'
