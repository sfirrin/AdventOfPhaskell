

def part1(inp):
    print('Part 1:')






def part2(inp):
    print('Part 2:')





def main():
    day = 0
    with open('in' + str(day).rjust(2, '0') + '.txt', 'rb') as f:
        inp = [line.strip() for line in f.readlines()]
    part1(inp)
    part2(inp)

main()