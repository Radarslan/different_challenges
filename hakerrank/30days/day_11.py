def get_valid_int(number, min, max):
    if min <= number <= max:
        return number
    return 0


if __name__ == '__main__':

    # arr = []

    # arr = [
    #     [1, 1, 1, 0, 0, 0],
    #     [0, 1, 0, 0, 0, 0],
    #     [1, 1, 1, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0],
    # ]

    # arr = [
    #     [1, 1, 1, 0, 0, 0],
    #     [0, 1, 0, 0, 0, 0],
    #     [1, 1, 1, 0, 0, 0],
    #     [0, 0, 2, 4, 4, 0],
    #     [0, 0, 0, 2, 0, 0],
    #     [0, 0, 1, 2, 4, 0],
    # ]

    arr = [
        [ -1,  1, -1,  0,  0, 0],
        [  0, -1,  0,  0,  0, 0],
        [ -1, -1, -1,  0,  0, 0],
        [  0, -9,  2, -4, -4, 0],
        [ -7,  0,  0, -2,  0, 0],
        [  0,  0, -1, -2, -4, 0],
    ]

    # for _ in range(6):
    #     arr.append(list(map(int, input().rstrip().split())))

    for row in arr:
        for element in row:
            element = get_valid_int(element, -9, 9)

    hourglass_sum = -65
    for i in range(4):
        for j in range(4):
            current_sum = 0
            current_sum += arr[i][j] + arr[i][j + 1] + arr[i][j + 2]
            current_sum += arr[i + 1][j + 1]
            current_sum += arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2]

            if current_sum > hourglass_sum:
                hourglass_sum = current_sum
    print(hourglass_sum)
