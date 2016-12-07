import re

def supports_tls(split_address):
    pattern = r'(\w)(\w)\2\1'
    reverse_pair = False
    for index, component in enumerate(split_address):
        found_items = re.findall(pattern, component)
        if found_items:
            if found_items[0][0] == found_items[0][1]:
                continue
            if index % 2 == 1:
                return False
            reverse_pair = True
    return reverse_pair

def supports_ssl(address):
    pt2pattern = r'(?:(\w)(\w)\1.*\[.*\2\1\2.*\])|(?:\[.*(\w)(\w)\3.*\].*\4\3\4)'
    split_address = re.split(r'\[|\]', address)

    for i in range(0, len(split_address), 2):
        for j in range(1, len(split_address), 2):
            combined_string = split_address[i] + '[' + split_address[j] + ']'

            match = re.findall(pt2pattern, combined_string)
            if match:
                uniques = set(match[0])
                if uniques > 2:
                    return True
    return False

def part1(inp):
    print('Part 1:')
    support_tls = []
    split_addresses = [re.split(r'\[|\]', addr) for addr in inp]
    supporting_tls = [addr for addr in split_addresses if supports_tls(addr)]
    supporting_ssl = [addr for addr in inp if supports_ssl(addr)]
    print(len(supporting_tls))

    print(len(supporting_ssl))





def part2(inp):
    print('Part 2:')





def main():
    day = 7
    with open('in' + str(day).rjust(2, '0') + '.txt', 'rb') as f:
        inp = [line.strip() for line in f.readlines()]
    part1(inp)
    part2(inp)

main()