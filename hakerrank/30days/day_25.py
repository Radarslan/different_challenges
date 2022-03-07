import cProfile
import pstats
import io


def profile(fnc):

    """A decorator that uses cProfile to profile a function"""

    def inner(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()
        retval = fnc(*args, **kwargs)
        pr.disable()
        s = io.StringIO()
        sortby = 'cumulative'
        ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
        ps.print_stats()
        print(s.getvalue())
        return retval

    return inner


def get_valid_int(number, min, max):
    try:
        number = int(number)
    except Exception as e:
        pass
    else:
        if min <= number <= max:
            return number
    return min


def get_divisors(number):
    divisors = [1, number]

    divisor_range_start = 2
    divisor_range_end = int(number ** 1/2 + 1)

    for divisor in range(divisor_range_start, divisor_range_end):
        if number % divisor == 0:
            divisors.append(divisor)
    return divisors


def is_prime(number):
    if number <= 3:
        return number > 1
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i ** 2 <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True


# def print_prime_or_not(numbers_to_test):


if __name__ == "__main__":
    # number_of_test_cases = input()
    # number_of_test_cases = get_valid_int(number_of_test_cases, 1, 30)
    # numbers_to_test = [
    #     get_valid_int(input(), 1,  10**9 * 2)
    #     for i in range(number_of_test_cases)
    # ]
    numbers_to_test = [
        1000000001,
        1000000002,
        1000000003,
        1000000004,
        1000000005,
        1000000006,
        1000000007,
        1000000008,
        1000000009,
        1000000010,
    ]
    cProfile.run('is_prime(numbers_to_test[0])')
    # for number in numbers_to_test:
    #     if is_prime(number):
    #         print("Prime")
    #     else:
    #         print("Not prime")

