def get_valid_int(number):
    if 0 <= number <= 100:
        return number
    return 0

class Difference:
    def __init__(self, a):
        self.__elements = a
        for element in self.__elements:
            self.get_valid_int(element, 1, 100)
        self.maximumDifference = 0

	# Add your code here
    @staticmethod
    def get_valid_int(number, min, max):
        if min <= number <= max:
            return number
        return 0

    def computeDifference(self):
        # for i in range(len(self.__elements)-1):
        #     for j in range(i+1, len(self.__elements)):
        #         difference = abs(self.__elements[i] - self.__elements[j])
        #         if difference > self.maximumDifference:
        #             self.maximumDifference = difference
        self.maximumDifference = max(self.__elements) - min(self.__elements)


# End of Difference class


_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
