#Write a python code to print 10 student details using class and lists

class Student:
    def __init__(self, name, roll_no, age, grade):
        self.name = name
        self.roll_no = roll_no
        self.age = age
        self.grade = grade

students = []
for i in range(10):
    name = input("Enter name of student {}: ".format(i+1))
    roll_no = input("Enter roll number of student {}: ".format(i+1))
    age = int(input("Enter age of student {}: ".format(i+1)))
    grade = input("Enter grade of student {}: ".format(i+1))
    students.append(Student(name, roll_no, age, grade))

print("Student details:")
for i, student in enumerate(students, start=1):
    print("Student {}: Name - {}, Roll No - {}, Age - {}, Grade - {}".format(i, student.name, student.roll_no, student.age, student.grade))
