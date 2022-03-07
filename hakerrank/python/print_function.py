if __name__ == '__main__':
    n = int(input())
    if n in range(1, 151):
        for i in range(1, n + 1):
            print(i, sep="", end="")
