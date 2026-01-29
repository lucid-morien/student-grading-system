from manager import StudentManager

def get_valid_name():
    while True:
        name = input("Enter student name: ").strip()
        if not name:
            print("Name cannot be empty.")
        elif not name.replace(" ", "").isalpha():
            print("Name must contain only letters.")
        else:
            return name


def get_valid_score():
    while True:
        try:
            score = float(input("Enter score (0 - 100): "))
            if 0 <= score <= 100:
                return score
            else:
                print("Score must be between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")


def show_menu():
    print("\n--- Student Grading System ---")
    print("1. Add student")
    print("2. Edit student")
    print("3. Delete student")
    print("4. Display students")
    print("5. Sort by name")
    print("6. Sort by score")
    print("7. Search student")
    print("8. Exit")

def main():
    manager = StudentManager()

    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            name = get_valid_name()
            score = get_valid_score()
            manager.add_student(name, score)
            print("Student added successfully.")

        elif choice == "2":
            try:
                student_id = int(input("Enter student ID: "))
                if student_id not in manager.students:
                    print("Student ID does not exist.")
                    continue
                name = get_valid_name()
                score = get_valid_score()
                manager.edit_student(student_id, name, score)
                print("Student updated.")
            except ValueError:
                print("Invalid ID.")

        elif choice == "3":
            try:
                student_id = int(input("Enter student ID: "))
                manager.delete_student(student_id)
            except ValueError:
                print("Invalid ID.")

        elif choice == "4":
            manager.display_students()

        elif choice == "5":
            manager.sort_by_name()
            print("Sorted by name.")

        elif choice == "6":
            manager.sort_by_score()
            print("Sorted by score.")

        elif choice == "7":
            print("\nSearch by:")
            print("1. ID")
            print("2. Name")

            option = input("Choose option: ").strip()

            if option == "1":
                try:
                    student_id = int(input("Enter student ID: "))
                    student = manager.search_by_id(student_id)
                    if student:
                        print("\nID | Name | Score | Grade")
                        print("-" * 30)
                        print(
                            f"{student.student_id} | {student.name} | {student.score} | {student.get_grade()}"
                        )
                    else:
                        print("Student not found.")
                except ValueError:
                    print("Invalid ID.")
            elif option == "2":
                name = input("Enter name to search: ").strip()
                results = manager.search_by_name(name)
                if results:
                    print("\nID | Name | Score | Grade")
                    print("-" * 30)
                    for student in results:
                        print(
                            f"{student.student_id} | {student.name} | {student.score} | {student.get_grade()}"
                        )
                else:
                    print("No matching students found.")

            else:
                print("Invalid search option.")
        
        elif choice == "8":
            print("Goodbye 👋")
            break

        else:
            print("Invalid choice. Please select 1–7.")

if __name__ == "__main__":
    main()
