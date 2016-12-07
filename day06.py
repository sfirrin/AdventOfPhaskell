import itertools


def day06(inp):
    column_chars = []
    for i in range(len(inp[0])):
        column_chars.append([c[i] for c in inp])
    most_freq = []
    least_freq = []
    for col in column_chars:
        counts = [(col.count(c), c) for c in set(col)]
        counts.sort(reverse=True)
        # print(counts)
        most_freq.append(counts[0])
        least_freq.append(counts[-1])
    pt1 = ''.join([tup[1] for tup in most_freq])
    print('Part 1:')
    print(pt1)
    pt2 = ''.join([tup[1] for tup in least_freq])
    print('Part 2:')
    print(pt2)


def main():
    day = 6
    with open('in' + str(day).rjust(2, '0') + '.txt', 'rb') as f:
        inp = [line.strip() for line in f.readlines()]
    day06(inp)

main()