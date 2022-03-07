def is_leap(year):
    if year in range(1900, 10 ** 5 + 1):
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            return True
    return False


year = int(input())
if year in range(1900, 10**5 + 1):
    print(is_leap(year))
