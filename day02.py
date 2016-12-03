
def day02a(inp):
    inp = [line.strip() for line in inp]
    bathroom_code = ''
    current = 5
    instruction_map = {'U': -3, 'R': 1, 'L': -1, 'D': 3}

    for line in inp:

        for char in line:

            if (char == 'U' and current <= 3) or \
               (char == 'R' and current in [3, 6, 9]) or \
               (char == 'L' and current in [1, 4, 7]) or \
               (char == 'D' and current >= 7):
                continue

            current += instruction_map[char]

        bathroom_code += str(current)

    print(bathroom_code)

def day02b(inp):
    inp = [line.strip() for line in inp]
    bathroom_code = ''
    # 0, 2 is the coordinate of 5
    x = 0
    y = 2
    keypad = [
        [None, None, '1', None, None],
        [None,  '2', '3',  '4', None],
        [ '5',  '6', '7',  '8',  '9'],
        [None,  'A', 'B',  'C', None],
        [None, None, 'D', None, None]
    ]

    for line in inp:

        for char in line:
            x_cand = x
            y_cand = y
            if char == 'U':
                y_cand = max(0, y - 1)
            if char == 'R':
                x_cand = min(4, x + 1)
            if char == 'L':
                x_cand = max(0, x - 1)
            if char == 'D':
                y_cand = min(4, y + 1)
            if keypad[y_cand][x_cand] is not None:
                x = x_cand
                y = y_cand


        bathroom_code += keypad[y][x]

    print(bathroom_code)

def main():
    with open('in02.txt', 'rb') as f:
        inp = f.readlines()
    day02a(inp)
    day02b(inp)

main()