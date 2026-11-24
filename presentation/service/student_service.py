
from repository.student_repository import StudentRepository


class StudentService:
    def __init__(self):
        self.repository = StudentRepository()

    def add_student(self, name, age):
        if not name.strip():
            raise ValueError("Студент аты бос болмауы керек")

        if age <= 0:
            raise ValueError("Жасы дұрыс көрсетілмеген")

        student = {
            "name": name,
            "age": age
        }

        return self.repository.add(student)

    def get_all_students(self):
        return self.repository.get_all()
