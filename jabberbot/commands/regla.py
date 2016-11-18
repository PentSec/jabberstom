import os
import re


def run_command(msg, *args):
    """Returns the available chickentag menu

    You can ask for a single meal: !chickentag H12"""
    chicken = [
        'r1 - Siempre darle la razon a Jeff',
        'r2 - Nunca Darle la razon a Edua4rd',
        'r3 - No confies en j3s']
    if args:
        try:
            index = int(re.findall(r"\d+", args[0])[0]) - 1
            return 'groupchat', chicken[index]
        except:
            pass
    return 'groupchat', os.linesep.join(chicken)
