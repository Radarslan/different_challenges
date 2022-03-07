def get_valid_integer(number):
    try:
        number = int(number)
        return number
    except Exception as e:
        return 0


if __name__ == '__main__':
    n = int(input())
    integer_list = [get_valid_integer(number) for number in input().split()]
    integer_tuple = tuple(integer_list)
    print(hash(integer_tuple))
