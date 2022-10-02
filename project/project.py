from student import Student
import csv
from tabulate import tabulate
import argparse
import sys


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", action="store_true")
    parser.add_argument("-a", action="store_true")
    args = parser.parse_args()
    if args.v:
        read_students_from_csv()
        sys.exit()
    elif args.a:
        fname = input("First name: ").strip().capitalize()
        lname = input("Last name: ").strip().capitalize()
        level = input("Level: ").capitalize()
        s = int(input("Science marks: "))
        m = int(input("Maths marks: "))
        e = int(input("English marks: "))

        if s < 0 or s > 100 or m < 0 or m > 100 or e < 0 or e > 100:
            sys.exit("\n Error: Marks can't be less than 0 and greater than 100!")

        info = [fname, lname, level]
        marks = {"science": s, "maths": m, "english": e}
        add_student(info, marks)

    else:
        print("\nWelcome to Grades50\n")
        print("OPTIONS:\n")

        options = []
        options.append(["Command", "Description"])
        options.append(["python project.py -v", "to view the list of students and their respective grades, gpa"])
        options.append(["python project.py -a", "to add a new student and calculate their grades, gpa"])
        print(tabulate(options, headers="firstrow", tablefmt="grid"))

def add_student(info, marks):
    student = Student(*info)
    student.set_marks(**marks)
    marks = student.get_marks()
    percentages = map(calculate_percentage, marks)
    percentages = list(percentages)
    grades = map(percent_to_grade, percentages)
    grades = list(grades)

    student.set_subject_grades(*grades)
    gpa = calculate_cgpa(*grades)
    student.set_gpa(gpa)

    # print(student)
    if not "pytest" in sys.modules:
        add_student_to_csv(student)

    students = []
    students.append(
        [
            "fname",
            "lname",
            "level",
            "science_grade",
            "maths_grade",
            "english_grade",
            "gpa",
        ]
    )
    students.append([*info, *grades, gpa])
    print("\nA new student has been added with following details:\n")
    print(tabulate(students, headers="firstrow", tablefmt="grid"))

    return student


def add_student_to_csv(student):
    file_name = "students.csv"
    try:
        with open(file_name, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(
                [
                    student.fname,
                    student.lname,
                    student.level,
                    *student.subject_grades(),
                    student.gpa,
                ]
            )

    except FileNotFoundError:
        sys.exit("File doesn't exist!")


def read_students_from_csv():
    file_name = "students.csv"
    try:
        students = []
        with open(file_name) as file:
            reader = csv.reader(file)
            for fname, lname, level, science_grade, maths_grade, english_grade, gpa in reader:
                students.append(
                    [
                        fname,
                        lname,
                        level,
                        science_grade,
                        maths_grade,
                        english_grade,
                        gpa,
                    ]
                )

    except FileNotFoundError:
        sys.exit("File doesn't exist!")

    print(tabulate(students, headers="firstrow", tablefmt="grid"))


def calculate_percentage(marks, total=100):
    return (marks / total) * 100


# https://www.jointread.com/grading-system-in-nepal/
def percent_to_grade(percent=0):
    if percent < 45:
        return "F"
    elif percent >= 45 and percent < 50:
        return "D"
    elif percent >= 50 and percent < 55:
        return "D+"
    elif percent >= 55 and percent < 60:
        return "C-"
    elif percent >= 60 and percent < 65:
        return "C"
    elif percent >= 65 and percent < 70:
        return "C+"
    elif percent >= 70 and percent < 75:
        return "B-"
    elif percent >= 75 and percent < 80:
        return "B"
    elif percent >= 80 and percent < 85:
        return "B+"
    elif percent >= 85 and percent < 90:
        return "A-"
    elif percent >= 90:
        return "A"


def grade_to_honor_point(grade):
    honor_points = {
        "A": 4,
        "A-": 3.7,
        "B+": 3.3,
        "B": 3,
        "B-": 2.7,
        "C+": 2.3,
        "C": 2,
        "C-": 1.7,
        "D+": 1.3,
        "D": 1,
        "F": 0,
    }

    return honor_points[grade]


def calculate_cgpa(science_g, maths_g, english_g):
    cgpa = (
        grade_to_honor_point(science_g)
        + grade_to_honor_point(maths_g)
        + grade_to_honor_point(english_g)
    ) / 3
    return round(cgpa, 2)


if __name__ == "__main__":
    main()
