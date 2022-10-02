from project import calculate_percentage, percent_to_grade, grade_to_honor_point, calculate_cgpa, add_student

def test_calculate_percentage():
    assert calculate_percentage(50) == 50
    assert calculate_percentage(0) == 0
    assert calculate_percentage(20, 50) == 40

def test_percent_to_grade():
    assert percent_to_grade() == "F"
    assert percent_to_grade(48) == "D"
    assert percent_to_grade(71) == "B-"
    assert percent_to_grade(97) == "A"
    assert percent_to_grade(66) == "C+"

def test_grade_to_honor_point():
    assert grade_to_honor_point("F") == 0
    assert grade_to_honor_point("C-") == 1.7
    assert grade_to_honor_point("B-") == 2.7
    assert grade_to_honor_point("D+") == 1.3
    assert grade_to_honor_point("A") == 4

def test_calculate_cgpa():
    assert calculate_cgpa("C-", "B", "C") == 2.23
    assert calculate_cgpa("A-", "A", "B+") == 3.67
    assert calculate_cgpa("C-", "D", "D+") == 1.33

def test_add_student():
    info = ["harry", "potter", "nine"]
    marks = {"science": 87, "maths": 97, "english": 83}
    student = add_student(info, marks)

    assert student.subject_grades() == ["A-", "A", "B+"]
    assert student.get_gpa() == 3.67