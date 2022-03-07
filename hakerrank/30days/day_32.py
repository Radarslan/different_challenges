from collections import defaultdict


def almostIncreasingSequence(sequence):
    if len(sequence) == 1:
        return True
    count_decrising_elements = 0
    i = 0
    limit = len(sequence) - 1
    while count_decrising_elements <= 1:
        if i >= limit:
            break
        if sequence[i] >= sequence[i + 1]:
            count_decrising_elements += 1
            if i > 0 and sequence[i - 1] >= sequence[i + 1]:
                sequence.pop(i + 1)
            else:
                sequence.pop(i)

            limit -= 1
        # elif i > 0 and count_decrising_elements == 1 and sequence[i-1] >= sequence[i]:
        #     count_decrising_elements += 1
        else:
            i += 1
    return count_decrising_elements == 1


def matrixElementsSum(matrix):
    sum = 0
    zeros = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] != 0:
                if (i == 0
                        or j not in zeros
                ):
                    sum += matrix[i][j]
            else:
                zeros.append(j)
    return sum


if __name__ == "__main__":
    # when the only element at the beginning
    # when the only element in the middle
    # when the only element at the end
    # when couple consequent elements at the beginning
    # when couple consequent elements in the middle
    # when couple consequent elements at the end
    # when one element at the beginning and one at the end
    # when one element at the beginning and one in the middle
    # when one element in the middle and one at the end

    # sequence = [1, 2, 1, 2]
    # # sequence = [10, 1, 2, 3, 4, 5]
    # # sequence = [40, 50, 60, 10, 20, 30]
    # # sequence = [1, 2, 3, 4, 5, 3, 5, 6]
    # # sequence = [1, 2, 3, 4, 3, 6]
    # print(almostIncreasingSequence(sequence))
    matrix = [[1, 1, 1, 0],
              [0, 5, 0, 1],
              [2, 1, 3, 10]]

    print(matrixElementsSum(matrix))
