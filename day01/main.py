#!/usr/bin/env python3

'''main module
'''


def pair(generator):
    ''' '''
    prev = next(generator)
    for curr in generator:
        yield prev, curr
        prev = curr


def triple(generator):
    ''' '''
    val1 = next(generator)
    val2 = next(generator)
    for val3 in generator:
        yield val1, val2, val3
        val1, val2 = val2, val3


if __name__ == '__main__':
    with open('./input', 'r', encoding='ascii') as fp:
        print('Part One: ', end='')
        print(sum(n > m for m, n in pair(map(int, fp))))
        fp.seek(0, 0)
        print('Part Two: ', end='')
        print(sum(n > m for m, n in pair(map(sum, triple(map(int, fp))))))