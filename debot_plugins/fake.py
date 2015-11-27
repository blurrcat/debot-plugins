#!/usr/bin/env python
# -*- coding: utf-8 -*-
from functools import partial

from faker import Faker

en_faker = Faker(locale='en')
cn_faker = Faker(locale='zh_CN')
usage = ('`provider [args,[args,...]]` - fake sth, try `name`, ' +
         '`address`, `image_url`')


def _main(faker, args):
    """
    `provider [args,[args,...]]` - fake sth, try `name`, `address`, `image_url`

    For a complete list of providers, see http://fake-factory.readthedocs.org/en/latest/providers.html
    """
    if not args:
        return
    parts = args.split(' ')

    if len(parts) == 1:
        provider, args = parts[0], ''
    elif len(parts) == 2:
        provider, args = parts
    else:
        return usage

    try:
        return getattr(faker, provider)(*[a for a in args.split(',') if a])
    except AttributeError:
        return 'No such provider: {}'.format(provider)
    except TypeError as e:
        return e.message



on_fake = partial(_main, en_faker)
on_fake_cn = partial(_main, cn_faker)

for f in (on_fake, on_fake_cn):
    f.__doc__ = _main.__doc__


if __name__ == '__main__':
    print(on_fake('name'))
    print(on_fake_cn('name'))
