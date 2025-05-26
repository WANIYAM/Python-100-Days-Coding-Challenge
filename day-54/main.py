# 54.Inheritance example: Person and Employee classes.

# Base class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

# Derived class (inherits from Person)
class Employee(Person):
    def __init__(self, name, age, employee_id, position):
        super().__init__(name, age)  # Call the constructor of Person
        self.employee_id = employee_id
        self.position = position

    def display_info(self):
        super().display_info()  # Call display_info of Person
        print(f"Employee ID: {self.employee_id}")
        print(f"Position: {self.position}")

# Example usage
person1 = Person("Alice", 30)
employee1 = Employee("Bob", 28, "E123", "Software Engineer")

print("Person Details:")
person1.display_info()

print("\nEmployee Details:")
employee1.display_info()
