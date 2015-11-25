#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import urllib

URL = 'http://dogr.io/'
NUM = 5


GROUPS = (
    (
        ('so', 'very', 'nice', 'sweet'),
        ('respect', 'doge', 'meme', 'intelligence', 'elegance', 'buy', 'vroom')
    ),
    (
        ('much', 'many', 'such'),
        ('noble', 'sleepy', 'sexy', 'legendary', 'fabulous', 'dangerous',
         'majestic', 'enticing', 'breathtaking', 'dignified')
    )
)
EXCLAMATIONS = ('wow', 'amaze', 'excite', 'neat')


def on_confess(sth='DecentFox'):
    """
    `sth` - make a doge confession about `sth`
    """
    phrases = [p.strip() for p in sth.split(',')]
    parts = set(phrases[1:])
    while len(parts) < NUM:
        a, b = random.choice(GROUPS)
        parts.add('{} {}'.format(random.choice(a), random.choice(b)))
    parts = [phrases[0]] + list(parts) + [random.choice(EXCLAMATIONS)]
    return '{}{}.png?split=false'.format(URL, urllib.quote('/'.join(parts)))


if __name__ == '__main__':
    url = on_confess()
    print url

