

def part1(inp):
    print('Part 1:')
    compressed_end_index = 0
    uncompressed = ''
    for index, char in enumerate(inp):
        if index >= compressed_end_index:
            if char == '(':
                index_of_close = inp.index(')', index, len(inp))
                inside_parens = inp[index+1:index_of_close]
                take = int(inside_parens.split('x')[0])
                repeats = int(inside_parens.split('x')[1])
                repeated = inp[index_of_close + 1: index_of_close + 1 + take]
                uncompressed += repeated * repeats
                compressed_end_index = index_of_close + 1 + take
                # print(take, len(repeated), repeated)
            else:
                uncompressed += char
    print(len(uncompressed))

def part2(inp):
    # print('Part 2:')
    compressed_end_index = 0
    uncompressed_len = 0
    for index, char in enumerate(inp):
        if index >= compressed_end_index:
            if char == '(':
                index_of_close = inp.index(')', index, len(inp))
                inside_parens = inp[index+1:index_of_close]
                take = int(inside_parens.split('x')[0])
                repeats = int(inside_parens.split('x')[1])
                repeated = inp[index_of_close + 1: index_of_close + 1 + take]
                # Recursive call
                uncompressed_len += part2(repeated) * repeats
                compressed_end_index = index_of_close + 1 + take
            else:
                uncompressed_len += 1
    return uncompressed_len




def main():
    day = 9
    with open('in' + str(day).rjust(2, '0') + '.txt', 'rb') as f:
        inp = [line.strip() for line in f.readlines()][0]
    part1(inp)
    print('Part 2:')
    print(part2(inp))

main()