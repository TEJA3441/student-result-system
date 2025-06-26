from database import setup_database, connect_db
from student import Student
from utils import get_valid_int, get_non_empty_input

def add_student():
    print("\n📥 Add New Student")
    name = get_non_empty_input("Enter name: ")
    roll = get_non_empty_input("Enter roll number: ")
    marks = get_valid_int("Enter marks (0-100): ")
    student = Student(name, roll, marks)
    student.save_to_db()

def view_students():
    print("\n📋 Student Records:")
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT name, roll_number, marks, grade FROM students")
    rows = cur.fetchall()
    if rows:
        for row in rows:
            print(f"Name: {row[0]}, Roll: {row[1]}, Marks: {row[2]}, Grade: {row[3]}")
    else:
        print("No records found.")
    conn.close()

def main():
    setup_database()
    while True:
        print("\n--- Student Result Management ---")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
