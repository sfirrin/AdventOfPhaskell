
def day03a(inp):
    dimensions = [dim.split() for dim in inp]
    # I heard you like list comprehensions
    int_dimensions = [sorted([int(item) for item in dimension]) for dimension in dimensions]
    return len([dim for dim in int_dimensions if (dim[0] + dim[1] > dim[2])])

def day03b(inp):
    dimensions = [dim.split() for dim in inp]
    int_dimensions = [[int(item) for item in dimension] for dimension in dimensions]
    valid_count = 0
    for i in range(0, len(int_dimensions), 3):
        for j in range(3):
            dims = [int_dimensions[i][j], int_dimensions[i+1][j], int_dimensions[i+2][j]]
            dims.sort()
            if dims[0] + dims[1] > dims[2]:
                valid_count += 1
    return valid_count

def main():
    with open('in03.txt', 'rb') as f:
        inp = f.readlines()
    print(day03a(inp))
    print(day03b(inp))

main()