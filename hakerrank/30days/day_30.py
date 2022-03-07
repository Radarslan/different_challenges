def checkPalindrome(inputString):
    string_length = len(inputString)
    middle = len(inputString) // 2
    part_1 = inputString[:middle]
    part_2 = inputString[-1:middle:-1]
    if string_length % 2 == 0:
        part_2 = inputString[-1:middle-1:-1]
    return part_1 == part_2


if __name__ == "__main__":
    s = input("enter a string: ")
    print(checkPalindrome(s))
