class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


def get_valid_int(number):
    if 0 <= number <= 100:
        return number
    return 0


def get_valid_string(string, length):
    if len(string) < 1:
        return ""
    return string[:length+1]


class Student(Person):
    def __init__(self, firstName, lastName, idNum, scores):
        firstName = get_valid_string(firstName, 10)
        lastName = get_valid_string(lastName, 10)
        idNum = get_valid_string(idNum, 7)
        super().__init__(firstName, lastName, idNum)
        for score in scores:
            score = get_valid_int(score)
        self.scores = scores

    def calculate(self):
        grade = "T"
        average_score = sum(scores) / len(scores)
        if 90 <= average_score <= 100:
            grade = "O"
        elif 80 <= average_score < 90:
            grade = "E"
        elif 70 <= average_score < 80:
            grade = "A"
        elif 55 <= average_score < 70:
            grade = "P"
        elif 40 <= average_score < 55:
            grade = "D"

        return grade


if __name__ == "__main__":
    line = input().split()
    firstName = line[0]
    lastName = line[1]
    idNum = line[2]
    numScores = int(input())  # not needed for Python
    scores = list(map(int, input().split()))
    s = Student(firstName, lastName, idNum, scores)
    s.printPerson()
    print("Grade:", s.calculate())
