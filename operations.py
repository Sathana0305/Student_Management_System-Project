from database import get_connection
def add_student():
    print("\n--- Add New Student ---")
    try:
        student_id = int(input("Enter student ID: "))
        name = input("Enter student name: ")
        department = input("Enter department: ")
        year = int(input("Enter year: "))
        marks = int(input("Enter marks: "))
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO students VALUES(?,?,?,?,?)",(student_id,name,department,year,marks))
        conn.commit()
        conn.close()
        print("Student added successfully!")
    except Exception as e:
        print("Something went wrong while adding student.")
        print("Reason:",e)
def view_students():
    print("\n-- Student List ---")
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM students")
    students=cursor.fetchall()
    if not students:
        print("No students found.")
    else:
        for student in students:
            print("ID:",student[0],
                  "Name:",student[1],
                  "Dept:",student[2],
                  "Year:",student[3],
                  "Marks:",student[4])
    conn.close()
def search_student():
    print("\n--- Search Student by ID ---")
    try:
        student_id=int(input("Enter student ID to search: "))
        conn=get_connection()
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM students WHERE student_id = ?",(student_id,))
        student=cursor.fetchone()
        if student:
            print("ID:", student[0],
                  "Name:", student[1],
                  "Dept:", student[2],
                  "Year:", student[3],
                  "Marks:", student[4])
        else:
            print("No student found with this ID.")
        conn.close()
    except Exception as e:
        print("Error occurred:", e)
def update_student():
    print("\n--- update_student ---")
    try:
        student_id=int(input("Enter student ID to update: "))
        conn=get_connection()
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM students WHERE student_id = ?",(student_id,))
        student=cursor.fetchone()
        if student:
            print("Current Details:")
            print("ID:", student[0],
                  "Name:", student[1],
                  "Dept:", student[2],
                  "Year:", student[3],
                  "Marks:", student[4])
            name=input("Enter new name: ")
            department=input("Enter new department: ")
            year_input=input("Enter new year: ")
            marks_input=input("Enter new marks: ")
            name=name if name else student[1]
            department=department if department else student[2]
            year=int(year_input) if year_input else student[3]
            marks=int(marks_input) if marks_input else student[4]
            cursor.execute("UPDATE students SET name=?, department=?, year=?, marks=? WHERE student_id=?",(name, department, year, marks, student_id))
            conn.commit()
            print("Student updated successfully!")
        else:
            print("No student found with this ID.")
        conn.close()
    except Exception as e:
        print("Error occurred:", e)
def delete_student():
    print("\n--- Delete Student ---")
    try:
        student_id=int(input("Enter student ID to delete: "))
        conn=get_connection()
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM students WHERE student_id=?", (student_id,))
        student=cursor.fetchone()
        if student:
            confirm=input("Are you sure you want to delete {student[1]}? (y/n): ")
            if confirm.lower() == 'y':
                cursor.execute("DELETE FROM students WHERE student_id=?", (student_id,))
                conn.commit()
                print("Student deleted successfully!")
            else:
                print("Deletion cancelled.")
        else:
            print("No student found with this ID.")
        conn.close()
    except Exception as e:
        print("Error occurred:", e)
