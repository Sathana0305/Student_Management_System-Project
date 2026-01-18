from database import create_student_table
from operations import add_student, view_students, search_student, update_student, delete_student
def start_app():
    print("Welcome to Student Management System")
    create_student_table()
    while True:
        print("\n1. Add Student")
        print("2. View Students")
        print("3. Search Student by ID")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Exiting application...")
            break
        else:
            print("Invalid choice. Try again.")
start_app()
