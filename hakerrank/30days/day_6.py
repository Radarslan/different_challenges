def get_valid_string(string):
    if len(string) < 2:
        return ""
    return string[:10001]


if __name__ == '__main__':
    number_of_test_cases = int(input())

    if number_of_test_cases:
        if number_of_test_cases > 10:
            number_of_test_cases = 10
        for n in range(1, number_of_test_cases+1):
            s = get_valid_string(input())
            even = []
            odd = []
            for i in range(0, len(s), 2):
                even += s[i]
                if i < len(s) - 1:
                    odd += s[i + 1]

            print(f"{''.join(even)} {''.join(odd)}")

# test cases
# s = ""
# t = 0
# t > 10
# t = 10
# t < 0
# s = "a"
# s = "ab"
