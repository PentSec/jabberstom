from datetime import datetime, timedelta
import random

min_delta = timedelta(hours=1)
start = datetime.now()
messages = [
    '{} Ha salido de la Sala!',
    'por suerte {} se fue voluntariamente',
    'por fin {} ha salido de la Sala',
    'Algo aqui {}',
    '{} Ha escapado sin ninguna patada',
]


def muc_got_offline(nick):
    global start
    if (datetime.now() - start) > min_delta:
        start = datetime.now()
        return random.choice(messages).format(nick)
