# Write a python code to find student from a given list using class

class Student:
    def __init__(self, name, roll_no, age, grade):
        self.name = name
        self.roll_no = roll_no
        self.age = age
        self.grade = grade

def find_student_by_roll(students, roll_no):
    for student in students:
        if student.roll_no == roll_no:
            return student
    return None

# Example usage:
students = [
    Student("Alice", "101", 18, "A"),
    Student("Bob", "102", 19, "B"),
    Student("Charlie", "103", 20, "C"),
]

roll_number = input("Enter roll number of the student you want to find: ")
found_student = find_student_by_roll(students, roll_number)
if found_student:
    print("Student found - Name: {}, Roll No: {}, Age: {}, Grade: {}".format(found_student.name, found_student.roll_no, found_student.age, found_student.grade))
else:
    print("Student with roll number {} not found.".format(roll_number))
