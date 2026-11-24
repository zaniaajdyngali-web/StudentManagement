from service.student_service import StudentService


def main():
    service = StudentService()

    while True:
        print("\n=== STUDENT MANAGEMENT SYSTEM ===")
        print("1. Студент қосу")
        print("2. Студенттер тізімі")
        print("3. Шығу")

        choice = input("Таңдаңыз: ")

        if choice == "1":
            name = input("Студент аты: ")
            age = int(input("Жасы: "))
            service.add_student(name, age)
            print("Студент сәтті қосылды!")

        elif choice == "2":
            students = service.get_all_students()
            for student in students:
                print(student)

        elif choice == "3":
            break


if __name__ == "__main__":
    main()
