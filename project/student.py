class Student:
    def __init__(self, fname, lname, level):
        self._fname = fname
        self._lname = lname
        self._level = level
        self._science = 0
        self._english = 0
        self._maths = 0
        self._science_grade = ""
        self._maths_grade = ""
        self._english_grade = ""
        self._gpa = 0

    def __str__(self):
        # print(self.size)
        return(f"{self._fname.capitalize()} {self._lname.capitalize()}: Class {self._level.capitalize()}\
             | Science: {self._science_grade} | Maths: {self._maths_grade} | English: {self._english_grade}\
                | GPA: {self._gpa}")

    def set_marks(self, science=0, maths=0, english=0):
        self._science = science
        self._maths = maths
        self._english = english

    def get_marks(self):
        return [self.science, self.maths, self.english]

    def set_subject_grades(self, science_grade="F", maths_grade="F", english_grade="F"):
        self._science_grade = science_grade
        self._maths_grade = maths_grade
        self._english_grade = english_grade

    def subject_grades(self):
        return [self._science_grade, self._maths_grade, self._english_grade]

    def set_gpa(self, gpa):
        self._gpa = gpa

    def get_gpa(self):
        return self._gpa

    @property
    def fname(self):
        return self._fname

    @property
    def lname(self):
        return self._lname

    @property
    def level(self):
        return self._level

    @property
    def science(self):
        return self._science

    @property
    def maths(self):
        return self._maths

    @property
    def english(self):
        return self._english

    @property
    def gpa(self):
        return self._gpa

