# 51.Create a class Student with attributes and methods to display details.
class Student:
    def __init__(self, name, roll_no, grade):
        self.name = name
        self.roll_no = roll_no
        self.grade = grade

    def display_details(self):
        print("Student Details:")
        print(f"Name     : {self.name}")
        print(f"Roll No. : {self.roll_no}")
        print(f"Grade    : {self.grade}")

# Example usage
student1 = Student("Alice", 101, "A")
student1.display_details()
