import math


@staticmethod
def find_greatest_common_divisor(number1, number2):
    if number2 == 0:
        return number1
    else:
        return number2


class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        return [self.real + no[0], self.imaginary + no[1]]

    def __sub__(self, no):
        return [self.real - no[0], self.imaginary - no[1]]

    def __mul__(self, no):
        return self._multiply_two_complex_numbers(
            number1=[self.real, self.imaginary],
            number2=no
        )

    @staticmethod
    def _multiply_two_complex_numbers(number1, number2):
        return [
            number1[0] * number2[0] + (-1) * number1[1] * number2[1],
            number1[0] * number2[1] + number1[1] * number2[0]
        ]

    def __truediv__(self, no):
        if no[0] != 0 and no[1] != 0:
            """
            Multiply the numerator and the denominator by the conjugate.
    
            :param no:
            :return:
            """
            #1
            numerator = self._multiply_two_complex_numbers(
                number1=[self.real, self.imaginary],
                number2=[no[0], (-1) * no[1]]
            )
            denominator = self._multiply_two_complex_numbers(
                number1=no,
                number2=[no[0], (-1) * no[1]]
            )
            return [self.real * no[0], self.imaginary * no[1]]
        raise ZeroDivisionError

    def mod(self):
        pass

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % self.real
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % self.imaginary
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result


if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x + y, x - y, x * y, x / y, x.mod(), y.mod()]), sep='\n')
