#!/usr/bin/env python
# encoding: utf-8
import string
import random

length = 10
n = 1000
filename = '02'


def generate_string(length):
    l = []
    for i in range(length):
        l.append(random.choice(string.ascii_lowercase))
    return ''.join(l)


def generate_move(length):
    start = random.randint(0, length - 1)
    end = random.randint(start, length - 1)
    insert = random.randint(0, length - end + start - 1)
    return start, end, insert

if __name__ == '__main__':
    with open(filename, 'w') as f:
        f.write(generate_string(length) + '\n')
        f.write(str(n) + '\n')
        for i in range(n):
            f.write('{0} {1} {2}\n'.format(*generate_move(length)))
