import sqlite3
from database import connect_db

class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks
        self.grade = self.calculate_grade()

    def calculate_grade(self):
        if self.marks >= 90:
            return 'A'
        elif self.marks >= 75:
            return 'B'
        elif self.marks >= 60:
            return 'C'
        elif self.marks >= 40:
            return 'D'
        else:
            return 'F'

    def save_to_db(self):
        conn = connect_db()
        cur = conn.cursor()
        try:
            cur.execute('''
                INSERT INTO students (name, roll_number, marks, grade)
                VALUES (?, ?, ?, ?)
            ''', (self.name, self.roll_number, self.marks, self.grade))
            conn.commit()
        except sqlite3.IntegrityError:
            print("❌ Roll number already exists.")
        finally:
            conn.close()
