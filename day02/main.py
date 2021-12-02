#!/usr/bin/env python3

'''main module
'''


if __name__ == '__main__':
    with open('input', 'r', encoding='ascii') as fp:
        depth, horizontal = 0, 0
        aim = 0
        for line in fp:
            steps = int(line.rpartition(' ')[2])
            if line.startswith('forward'):
                horizontal += steps
                depth += aim * steps
            elif line.startswith('up'):
                depth -= steps
                aim -= steps
            elif line.startswith('down'):
                depth += steps
                aim += steps
        print(horizontal * depth)