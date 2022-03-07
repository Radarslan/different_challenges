def get_valid_string(string):
    if len(string) not in range(1, 1000):
        return ""
    return string


def validate_string(string):
    string = get_valid_string(string)
    string_methods = [
        str.isalnum,
        str.isalpha,
        str.isdigit,
        str.islower,
        str.isupper
    ]

    for method in string_methods:
        check = False
        for character in string:
            if method(character):
                check = True
                break
        print(check)



if __name__ == '__main__':
    s = input()
    validate_string(s)
