def get_valid_string(string):
    if len(string) not in range(1, 200):
        return ""
    return string


def count_substring(string, sub_string):
    string = get_valid_string(string)
    sub_string = get_valid_string(sub_string)
    number_of_times = 0
    for i in range(0, len(string)):
        if string[i:i+len(sub_string)] == sub_string:
            number_of_times += 1
    return number_of_times


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
