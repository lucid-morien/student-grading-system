class Student():
    def __init__(self, student_id, name, score):
        self.id = student_id
        self.name = name
        self.score = score



    def get_grade(self):
        if self.score >= 80:
            return "A"
        elif self.score >= 70:
            return "B"
        elif self.score >= 60:
            return "C"
        elif self.score >= 50:
            return "D"
        else:
            return "F"

    def to_string(self):
        return f"{self.student_id}, {self.name},{self.score}"