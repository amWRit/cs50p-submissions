# GRADES50
## Video Demo:  <https://youtu.be/9O8SVDo2-4M>
## Description:
__GRADES50__ is a subject gradepoint and gpa calculator. It has two main features:
- python __project.py -v__ --> User can view the list of students and their respective subject grades and gpa.
- python __project.py -a__ --> User can add a new student to the list of students and their respective subject grades and gpa.
    - If the user chooses this option, they are asked to input first name, last name, and marks of science, maths and english subjects.
    - The program calculates grades for each subject and the gpa.
    - Then the student is added to list of students in a CSV file.
- If the user doesn't input __-v__ or __-a__, the program shows the correct usage and exits.

## Files:
### student.py
- This file contains the class declaration and methods related to Student Class.
- The __init__ method expects only fname, lname and level during object instantation.
- Other important methods are set_marks, get_marks, set_subject_grades and subject_grades.


### students.csv
- This CSV file contains all the students added by the user.
- It contains: __fname, lname, level, science_grade, maths_grade, english_grade and gpa__.


### project.py
- This is the main file where the program executes.
- Users have options to either view students' list (-v) or add a student (-a).
- argparse has been used to parse the arguments.
- If the user chooses to add a new student, they are asked to input first name, last name, and marks of science, maths and english subjects.
- If the marks are not in between 0 and 100 (inclusive), the program exits.
- It contains the following functions related to calculation:
    - calculate_percentage: given marks and optionally total (default is 100), it calculates percentage.
    - percent_to_grade: converts percentage into letter grade based on this <https://www.jointread.com/grading-system-in-nepal/>
    - grade_to_honor_point: converts letter grades to points.
    - calculate_cgpa: calculates cgpa based on grade points of three subjects.
- It also contains following functions:
    - add_student: creates a new student with given inputs - calculates letter grades and gpa; then adds them to student
    - add_student_to_csv: add the new created student's details into students.csv with this format: fname, lname, level, science_grade, maths_grade, english_grade and gpa
    - read_students_from_csv: reads all the students' details from csv and prints them in a tabulated format using tabulate.

### test_project.py
- This file, as the name suggests, is for testing purposes.
- It tests these functions: calculate_percentage, percent_to_grade, grade_to_honor_point, calculate_cgpa, add_student

### Notes
- As I was testing __add_student__ in test_project.py, a new student was being created and added to the CSV. So I google to see if there was a way to stop this particular function if we are running only test. Interestingly when we run pytest test_project.py, __pytest__ is present in sys.modules. Then __add_student__ would run only if __pytest__ was not present in sys.modules. Voila!
- Using __map__ was quite fun. It really decreases the lines.
- I also tried using unpacking with __*__ and __**__.