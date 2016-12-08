from pprint import pprint
import numpy as np

def day08(inp):
    screen = np.array([[False]*6] * 50)
    for instr in inp:
        split_instr = instr.split()
        if split_instr[0] == 'rect':
            xy = split_instr[1].split('x')
            xy = [int(val) for val in xy]
            screen[:xy[0], :xy[1]].fill(True)
        elif split_instr[0] == 'rotate':
            distance = int(split_instr[-1])
            row_column = int(split_instr[2][2:])
            if split_instr[1] == 'column':
                screen[row_column, :] = np.roll(screen[row_column, :], distance)
            else:
                screen[:, row_column] = np.roll(screen[:, row_column], distance)

    print('Part 1:')
    print(np.sum(screen))

    print('Part 2:')
    for row in range(6):
        row_string = ''
        for item in screen[:, row]:
            row_string += ' ' if not item else '#'
        print(row_string)




def main():
    day = 8
    with open('in' + str(day).rjust(2, '0') + '.txt', 'rb') as f:
        inp = [line.strip() for line in f.readlines()]
    day08(inp)

main()