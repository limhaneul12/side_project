class Score:
    def __init__(self, korean, english, math, social, science, time):
        self.korean = korean
        self.english = english
        self.math = math
        self.social = social
        self.science = science
        self.time = time

    # 총합
    def get_sum(self):
        return self.korean + self.english +\
               self.math + self.social + self.science
    # 평균
    def get_average(self):
        return self.get_sum() / 5

    # 등급
    def get_grade(self):
        if self.get_average() >= 90:
            grade = "A"
        elif self.get_average() >= 80:
            grade = "B"
        elif self.get_average() >= 70:
            grade = "C"
        elif self.get_average() >= 60:
            grade = "D"
        else:
            grade = "F"

        return grade

students = [
    Score(55, 60, 60, 40, 50, 3),
    Score(60, 70, 90, 100, 80, 20),
    Score(90, 95, 93, 89, 100, 77),
    Score(80, 83, 90, 94, 100, 50)
]

for student in students:
    print(student.get_grade())