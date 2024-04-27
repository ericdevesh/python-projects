#Write a python code to inherit employee class to student class

class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

class Student(Employee):
    def __init__(self, name, emp_id, roll_no, age, grade):
        super().__init__(name, emp_id)
        self.roll_no = roll_no
        self.age = age
        self.grade = grade

# Example usage:
student = Student("Alice", "E101", "101", 18, "A")
print("Student Name:", student.name)
print("Student Employee ID:", student.emp_id)
print("Student Roll No:", student.roll_no)
print("Student Age:", student.age)
print("Student Grade:", student.grade)
