def shapeArea(n):
    #n1, 2, 3,  4,  5
    # 1, 5, 13, 25, 41
    #   4, 8, 12, 16
    # if n == 1:
    #     return n
    area = 1
    for i in range(2, n+1):
        area += 4 * (i - 1)
    return area


def makeArrayConsecutive2(statues):
    statues = sorted(statues)
    additional_statues = []
    for i in range(len(statues)-1):
        filled_the_gaps = False
        gap_filler = statues[i] + 1
        while not filled_the_gaps:
            if statues[i+1] - gap_filler > 0:
                additional_statues.append(gap_filler)
                gap_filler += 1
            elif statues[i+1] - gap_filler == 0:
                filled_the_gaps = True
    return len(additional_statues)


if __name__ == "__main__":
    # for i in range(1, 10):
    #     print(shapeArea(i))

    statues = [6, 2, 3, 8]
    print(makeArrayConsecutive2(statues))


