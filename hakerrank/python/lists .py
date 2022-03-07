def get_valid_integer(number):
    try:
        number = int(number)
        return number
    except Exception as e:
        return 0

if __name__ == '__main__':
    N = int(input())
    l = []
    for number in range(N):
        command = input()
        command = command.split()
        operation = command.pop(0)
        if operation != "print":
            operands = [get_valid_integer(int(operand)) for operand in command]
            l.__getattribute__(operation).__call__(*operands)
        else:
            print(l)