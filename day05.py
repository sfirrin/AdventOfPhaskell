import hashlib

def day05a(inp):
    password = ''
    index = 0
    while len(password) < 8:
        md5 = hashlib.md5()
        md5.update(inp + str(index))
        hashed = md5.hexdigest()
        if hashed[:5] == '00000':
            password += hashed[5]
            print(password)
        index += 1
    print('The final password is: ' + password)

def day05b(inp):
    password = 8 * [' ']
    found_chars = 0
    index = 0
    while found_chars < 8:
        md5 = hashlib.md5()
        md5.update(inp + str(index))
        hashed = md5.hexdigest()
        if hashed[:5] == '00000':
            passindex = int(hashed[5], 16)
            if passindex < 8 and password[passindex] == ' ':
                password[passindex] = hashed[6]
                found_chars += 1
                print(password)
        index += 1
    print(''.join(password))

def main():
    with open('in05.txt', 'rb') as f:
        inp = f.read()
    print('Part 1:')
    day05a(inp)
    print('Part 2:')
    day05b(inp)

main()