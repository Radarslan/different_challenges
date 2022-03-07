class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError


class Calculator(AdvancedArithmetic):

    @staticmethod
    def get_valid_int(number, min, max):
        if min <= number <= max:
            return number
        return 1

    # def get_divisors(self, n, divisor):
    #     if divisor in [0, 1]:
    #         return 0
    #     if n % divisor == 0:


    def divisorSum(self, n):
        n = self.get_valid_int(n, 1, 1000)
        if n == 1:
            return 1
        s = 1 + n
        divisor_range_start = 2
        divisor_range_end = n
        if n % divisor_range_start == 0:
            s += divisor_range_start
            divisor_range_end = n // divisor_range_start + 1
            divisor_range_start = 3

        for divisor in range(divisor_range_start, divisor_range_end):
            if n % divisor == 0:
                s += divisor
        return s


n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)