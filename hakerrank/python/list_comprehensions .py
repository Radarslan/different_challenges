def get_valid_integer(number):
    try:
        number = int(number)
        return number
    except Exception as e:
        return 0


def get_all_permutations(numbers):
    return [
        [i, j, k]
        for i in range(numbers[0] + 1)
        for j in range(numbers[1] + 1)
        for k in range(numbers[2] + 1)
    ]


def remove_all_that_sum_up_to_n(permutations):
    return [
        coordinates
        for coordinates in permutations
        if sum(coordinates) != n
    ]


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    numbers = []
    for number in [x, y, z]:
        numbers.append(get_valid_integer(number))
    permutations = get_all_permutations(numbers)
    print(remove_all_that_sum_up_to_n(permutations))
