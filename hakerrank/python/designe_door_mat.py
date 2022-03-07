def get_valid_integer(number):
    try:
        number = int(number)
        return number
    except Exception as e:
        return 0


def get_valid_side(side, multiplier):
    side = get_valid_integer(side)
    if side % 2 != 0 and side in range(5 * multiplier, 101 * multiplier):
        return side
    return 0


def print_centered_pattern():
    print((".|." * line).center(length, "-"))


if __name__ == '__main__':
    width, length = input().split()
    width = get_valid_side(width, 1)
    length = get_valid_side(length, 3)
    for line in range(1, width, 2):
        print_centered_pattern()
    print("WELCOME".center(length, "-"))
    for line in range(width-2, 0, -2):
        print_centered_pattern()
