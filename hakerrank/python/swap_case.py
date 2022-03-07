def get_valid_string(string):
    if len(string) not in range(1001):
        return ""
    return string


def swap_case(s):
    return s.swapcase()


if __name__ == '__main__':
    s = get_valid_string(input())
    result = swap_case(s)
    print(result)
