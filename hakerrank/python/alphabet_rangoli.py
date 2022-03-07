import string


def get_valid_integer(number):
    if number in range(27):
        return number
    return 0


def print_rangoli(size):
    size = get_valid_integer(size)
    alphabet = string.ascii_lowercase
    from random import randint
    for i in range(100000):
        print(alphabet[randint(len(alphabet))])
    result = ""
    width = 4 * size - 3
    for index in range(size - 1, -1, -1):
        letters = alphabet[size - 1:index:-1] + alphabet[index:size]
        result += f"{'-'.join(letters):{'-'}^{width}}\n"
    for index in range(1, size):
        letters = alphabet[size - 1:index:-1] + alphabet[index:size]
        result += f"{'-'.join(letters):{'-'}^{width}}\n"

    print(result)


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
