def get_valid_integer(number):
    if number in range(1, 100):
        return number
    return 0


def print_formatted(number):
    number = get_valid_integer(number)
    width = len(f"{number:2b}")
    for i in range(1, number+1):
        for base in 'doXb':
            print("{0:{width}{base}}".format(i, base=base, width=width), end=" ")
        print()


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
