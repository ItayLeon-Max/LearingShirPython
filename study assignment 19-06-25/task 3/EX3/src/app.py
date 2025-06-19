def get_average_by_course_in_year(students: list, course: str, year: int) -> float:
    # return the average of a specific course in a specific year
    total, count = 0, 0
    for record in students:
        c, y, sem, sid, grade = record.split(',')
        if c == course and int(y) == year:
            total += int(grade)
            count += 1
    return total / count if count > 0 else 0


def get_average_by_course_in_year_at_semester(students: list, course: str, year: int, semester: str) -> float:
    # return the average of a specific course in a specific year and specific semester
    total, count = 0, 0
    for record in students:
        c, y, sem, sid, grade = record.split(',')
        if c == course and int(y) == year and sem.lower() == semester.lower():
            total += int(grade)
            count += 1
    return total / count if count > 0 else 0


def get_average_by_student_id(students: list, student_id: str) -> float:
    # return the average of a specific student in all courses they took
    total, count = 0, 0
    for record in students:
        c, y, sem, sid, grade = record.split(',')
        if sid == student_id:
            total += int(grade)
            count += 1
    return total / count if count > 0 else 0


if __name__ == "__main__":  # DO NOT DELETE THIS LINE
    # Your main program
    # Use it to test your program by invoking the calls of your choice.
    # Respect this level of indentation.
    grades = [
        "Java,2022,summer,s1,75",
        "Java,2022,summer,s1,80",
        "Java,2022,summer,s2,81",
        "Java,2022,summer,s3,93",
        "Java,2022,summer,s4,87",
        "Java,2022,summer,s5,88",
        "Java,2022,summer,s6,90",
        "Java,2022,summer,s7,84",
        "Java,2022,summer,s8,95",
        "Java,2022,summer,s9,91",
        "Java,2022,summer,s10,77",
        "Java,2022,summer,s11,74",
        "Java,2022,summer,s12,81",
        "Java,2022,spring,s1,85",
        "Java,2022,spring,s2,77",
        "Java,2022,spring,s3,90",
        "Java,2022,spring,s4,95",
        "Java,2022,spring,s5,78",
        "Java,2022,spring,s6,83",
        "Java,2022,spring,s7,92",
        "Java,2022,spring,s8,84",
        "Java,2022,spring,s9,91",
        "Java,2022,spring,s10,87",
        "Java,2022,spring,s11,88",
        "Java,2022,spring,s12,85",
        "Java,2021,summer,s1,88",
        "Java,2021,summer,s2,75",
        "Java,2021,summer,s3,80",
        "Java,2021,summer,s4,82",
        "Java,2021,summer,s5,84",
        "Java,2021,winter,s1,90",
        "Java,2021,winter,s2,85",
        "Java,2021,winter,s3,83",
        "Assembly,2021,summer,s1,77",
        "Assembly,2021,summer,s2,91",
        "Assembly,2021,summer,s3,84",
        "Assembly,2021,summer,s4,95",
        "Assembly,2021,spring,s1,89",
        "Assembly,2021,spring,s2,83",
        "Assembly,2021,spring,s3,94",
        "Assembly,2021,spring,s4,88",
        "Cobol,2020,spring,s1,75",
        "Cobol,2020,spring,s2,84"
    ]

    print("Calculating average for Java course, year 2022/summer:")
    print(get_average_by_course_in_year_at_semester(grades, 'Java', 2022, 'summer'))

    print("Calculating average for Java course, year 2022/spring:")
    print(get_average_by_course_in_year_at_semester(grades, 'Java', 2022, 'spring'))

    print("Calculating average for Java course, year 2022:")
    print(get_average_by_course_in_year(grades, 'Java', 2022))

    print("Calculating average for Java course, year 2021:")
    print(get_average_by_course_in_year(grades, 'Java', 2021))

    print("Calculating average for student s1:")
    print(get_average_by_student_id(grades, 's1'))

    print("Calculating average for student s2:")
    print(get_average_by_student_id(grades, 's2'))