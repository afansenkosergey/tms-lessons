from student import Student

students = [Student('Anna', 10),
            Student('Viktor', 5),
            Student('Misha', 7),
            Student('Vera', 8),
            Student('Maria', 9)]


def calc_sum_scholarship(students):
    total_scholarship = 0
    for student in students:
        total_scholarship += student.get_scholarship()
    return f'{total_scholarship} рублей.'


def get_excellent_student_count(students):
    excellent_count = 0
    for student in students:
        if student.is_excellent():
            excellent_count += 1
    return excellent_count


print(calc_sum_scholarship(students))
print(get_excellent_student_count(students))
