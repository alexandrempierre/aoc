#!/usr/bin/env python3

'''main module
'''


def frequency_count(value, table=None):
    if table is None:
        table = [{'0': 0, '1': 0} for c in value]
    for idx, c in enumerate(value):
        table[idx][c] += 1
    return table

def gamma(table):
    binary_str = ''.join('0' if pos['0'] > pos['1'] else '1' for pos in table)
    return int(binary_str, 2)


def eps(table):
    binary_str = ''.join('0' if pos['0'] < pos['1'] else '1' for pos in table)
    return int(binary_str, 2)

if __name__ == '__main__':
    with open('input', 'r', encoding='ascii') as fp:
        table = None
        for line in fp:
            table = frequency_count(line.strip(), table)
        print(gamma(table) * eps(table))