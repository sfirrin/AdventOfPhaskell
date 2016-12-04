
def day04a(inp):
    sector_id_sum = 0
    real_data = []
    for l in inp:
        char_to_freq = {}
        for char in l:
            if char.isdigit():
                break
            if char == '-':
                continue
            char_to_freq[char] = char_to_freq.get(char, 0) + 1
        freq_tuples = sorted(char_to_freq.items(), key=lambda k : k[0])
        freq_tuples.sort(key=lambda k : k[1], reverse=True)
        most_frequent = [tup[0] for tup in freq_tuples[:5]]
        correct_checksum = reduce(lambda x, y : x+y, most_frequent, '')

        # print(l)
        actual_checksum = l.split('[')[1][:-1]
        # print(actual_checksum)

        sector_id = [char for char in l if char.isdigit()]
        sector_id = int(reduce(lambda x, y : x+y, sector_id, ''))

        # print(correct_checksum)
        if actual_checksum == correct_checksum:
            sector_id_sum += sector_id

        real_data.append(l)

    print(sector_id_sum)
    return real_data

def day04b(real_data):
    # print(real_data)
    for data in real_data:
        sector_id = [char for char in data if char.isdigit()]
        sector_id = int(reduce(lambda x, y: x + y, sector_id, ''))
        decoded = ''

        for char in data:
            if char.isdigit():
                break
            if char == '-':
                decoded += ' '
                continue
            value = (ord(char) - 97 + sector_id) % 26
            decoded += chr(value + 97)

        if 'north' in decoded and 'pole' in decoded:
            print(decoded + ' ' + str(sector_id))


def main():
    with open('in04.txt', 'rb') as f:
        inp = [line.strip() for line in f.readlines()]
    real_data = day04a(inp)
    day04b(real_data)

main()