def sum_of_digits(number):
    summ = 0
    while number > 0:
        summ += number % 10
        number = number // 10
    return summ


def isLucky(n):
    string_n = str(n)
    half_1 = string_n[:len(string_n) // 2]
    half_2 = string_n[len(string_n) // 2:]
    sum_half_1 = sum_of_digits(int(half_1))
    sum_half_2 = sum_of_digits(int(half_2))
    return sum_of_digits(int(half_1)) == sum_of_digits(int(half_2))


def sortByHeight(a):
    sorted_array = sorted(a)
    start = 0
    for i in range(len(sorted_array)):
        if sorted_array[i] != -1:
            start = i
            break
    sorted_array = sorted_array[start:]
    for i in range(len(a)):
        if a[i] != -1:
            a[i] = sorted_array.pop(0)
    return a


def reverseInParentheses(inputString):
    # find all parentheses
    #
    parentheses = {
        "(": [],
        ")": []
    }
    start = end = 0
    result_string = ""
    temp_string = ""
    for i in range(len(inputString)):
        if inputString[i] == "(":
            parentheses["("].append(i)
            if result_string == "":
                result_string += inputString[:i]
        if inputString[i] == ")":
            # parentheses[")"].append(i)
            start = parentheses["("].pop()
            # end = parentheses[")"].pop()
            if temp_string == "":
                temp_string = inputString[start + 1:i][::-1]
            else:
                temp_string = f"{inputString[start + 1:i][::-1]}{temp_string}"[::-1]
            result_string += inputString[:start] + inputString[start + 1:i][::-1]
    for i in range(len(parentheses["("])):
        result_string += (
                inputString[:parentheses["("][i]]
                + inputString[parentheses["("][i]:parentheses[")"][i]][::-1]
        )
        # result_string +=

    return result_string


if __name__ == "__main__":
    # print(isLucky(12343214))
    # print(sortByHeight([-1, 150, 190, 170, -1, -1, 160, 180]))
    print(reverseInParentheses("foo(bar(baz))blim"))
