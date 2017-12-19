#!/usr/bin/env python3
import random

rnd = random.SystemRandom()

CALENDAR_FACTS = (
        'Did you know that',
        [
            (
                'the',
                ['fall', 'spring'],
                'equinox'
            ),
            (
                'the',
                ['winter', 'summer'],
                ['solstice', 'olympics'],
            )
        ],
        [
            (
                'happens',
                ['earlier', 'later', 'at the wrong time'],
                'every year'
            ),
            (
                'might',
                ['not happen', 'happen twice'],
                'this year'
            )
        ]
)


def generate(tree):
    for part in tree:
        if isinstance(part, tuple):
            yield from generate(part)
        elif isinstance(part, list):
            c = choice(part)
            if isinstance(c, str):
                yield c
            else:
                yield from generate(c)
        elif isinstance(part, str):
            yield part


def choice(options):
    return rnd.choice(options)


def main():
    from argparse import ArgumentParser
    parser = ArgumentParser()
    args = parser.parse_args()
    fact = list(generate(CALENDAR_FACTS))
    print(' '.join(fact))


if __name__ == '__main__':
    main()
