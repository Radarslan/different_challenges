def get_students_with_second_lowest_grade(records):
    if len(records) in range(2, 6):
        scores = {}
        for record in records:
            if record[1] not in scores:
                scores[record[1]] = []
            scores[record[1]].append(record[0])

        second_lowest_score = get_second_lowest_score(list(scores.keys()))
        return sorted(scores[second_lowest_score])


def get_second_lowest_score(arr):
        arr = sorted(arr)
        for i in range(1, len(arr)):
            if arr[i] != arr[0]:
                return arr[i]
        return arr[0]


if __name__ == '__main__':
    records = []
    number = 5
    names = ["Harry", "Berry", "Tina", "Akriti", "Harsh"]
    scores = [37.21, 37.21, 37.2, 41, 39]
    for _ in range(number):
        records.append([names[_], scores[_]])
    for name in get_students_with_second_lowest_grade(records):
        print(name)
