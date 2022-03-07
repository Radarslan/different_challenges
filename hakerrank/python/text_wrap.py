import textwrap


def get_valid_string(string):
    if len(string) not in range(1, 1000):
        return ""
    return string


def get_valid_integer(width, string_length):
    if width in range(1, string_length):
        return width
    return 0


def wrap(string, max_width):
    string = get_valid_string(string)
    max_width = get_valid_integer(max_width, len(string))
    return "\n".join(textwrap.wrap(string, max_width))


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
