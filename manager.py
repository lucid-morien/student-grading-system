from student import Student
import os

from student import Student
import os

class StudentManager:
    def __init__(self, filename="data.txt"):
        self.filename = filename
        self.students = {}
        self.load_from_file()

    def generate_id(self):
        if not self.students:
            return 1
        return max(self.students.keys()) + 1

    def add_student(self, name, score):
        student_id = self.generate_id()
        self.students[student_id] = Student(student_id, name, score)
        self.save_to_file()

    def edit_student(self, student_id, name, score):
        if student_id in self.students:
            self.students[student_id].name = name
            self.students[student_id].score = score
            self.save_to_file()
        else:
            print("Student not found.")

    def delete_student(self, student_id):
        if student_id in self.students:
            del self.students[student_id]
            self.save_to_file()
        else:
            print("Student not found.")

    def display_students(self):
        if not self.students:
            print("No students available.")
            return

        print("\nID | Name | Score | Grade")
        print("-" * 30)
        for student in self.students.values():
            print(
                f"{student.student_id} | {student.name} | {student.score} | {student.get_grade()}"
            )

    def sort_by_name(self):
        self.students = dict(
            sorted(self.students.items(), key=lambda item: item[1].name.lower())
        )

    def sort_by_score(self):
        self.students = dict(
            sorted(self.students.items(), key=lambda item: item[1].score, reverse=True)
        )

    def save_to_file(self):
        with open(self.filename, "w") as file:
            for student in self.students.values():
                file.write(student.to_string() + "\n")

    def load_from_file(self):
        if not os.path.exists(self.filename):
            return

        with open(self.filename, "r") as file:
            for line in file:
                student_id, name, score = line.strip().split(",")
                student_id = int(student_id)
                score = float(score)
                self.students[student_id] = Student(student_id, name, score)

    def search_by_id(self, student_id):
        return self.students.get(student_id)


    def search_by_name(self, name):
        results = []
        name = name.lower()
        for student in self.students.values():
            if name in student.name.lower():
                results.append(student)
        return results
