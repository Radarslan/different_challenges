def merge_the_tools(string, k):
    # your code goes here
    from collections import OrderedDict
    for i in range(0, len(string), k):
        print("".join(OrderedDict.fromkeys(string[i:i + k]).keys()))


if __name__ == '__main__':
    # string, k = input(), int(input())
    string = "AABCAAADA"
    k = 3
    merge_the_tools(string, k)
