def get_average_score(marks):
    if len(marks) == 3:
        summ = 0
        for mark in marks:
            if mark >= 0 and mark <= 100:
                summ += mark
        return summ / len(marks)


if __name__ == '__main__':
    # n = 3
    # student_marks = {
    #     "Krishna": [67, 68, 69],
    #     "Arjun": [70, 98, 63],
    #     "Malika": [52, 56, 60],
    # }
    # query_name = "Malika"
    n = 2
    student_marks = {
        "Harsh": [25, 26.5, 28],
        "Anurag": [26, 28, 30],
    }
    query_name = "Harsh"

    if n in range(2, 11) and query_name in student_marks:
        average_score = get_average_score(student_marks[query_name])
        print(f"{average_score:.2f}")
