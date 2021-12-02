#!/usr/bin/env python3

'''main module
'''


def pair(generator):
    ''' '''
    prev = next(generator)
    for curr in generator:
        yield prev, curr
        prev = curr


if __name__ == '__main__':
    with open('./input', 'r', encoding='ascii') as fp:
        print(sum(n > m for m, n in pair(map(int, fp))))