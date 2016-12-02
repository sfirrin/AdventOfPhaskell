
def day01():
    # This is why it's not a good idea to write code at 12am lol
    with open('in01.txt', 'rb') as f:
        inp = f.read()

    spl_inp = inp.split(', ')
    # print(spl_inp)
    direction = 0
    x = 0
    y = 0

    coord_set = set()
    coord_set.add((0, 0))
    for ins in spl_inp:
        print(ins)
        dir = ins[0]
        dist = int(ins[1:])
        prev_x = x
        prev_y = y
        if dir == 'L':
            direction -= 1
        else:
            direction += 1

        if direction == -1:
            direction = 3
        if direction == 4:
            direction = 0
        print(direction)
        if direction == 0:
            y += dist
            for yi in range(prev_y+1, y+1):
                # print(x, yi)
                if (x, yi) in coord_set:
                    print ('found')
                    print(x, yi)
                    print(x + yi)
                    return
                coord_set.add((x, yi))
        if direction == 1:
            x += dist
            for xi in range(prev_x+1, x+1):
                if (xi, y) in coord_set:
                    print('found')
                    print(xi, y)
                    print(xi + y)
                    return
                coord_set.add((xi, y))
        if direction == 2:
            y -= dist
            for yi in range(y, prev_y):
                if (x, yi) in coord_set:
                    print('found')
                    print(x, yi)
                    print(x+yi)
                    return
                coord_set.add((x, yi))
        if direction == 3:
            x -= dist
            for xi in range(x, prev_x):
                if (xi, y) in coord_set:
                    print('found')
                    print(xi, y)
                    print(xi + y)
                    return
                coord_set.add((xi, y))


day01()
