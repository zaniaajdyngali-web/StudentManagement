
class StudentRepository:
    def __init__(self):
        self.students = []

    def add(self, student):
        student["id"] = len(self.students) + 1
        self.students.append(student)
        return student

    def get_all(self):
        return self.students
