# 55.Method overriding in derived class.

class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):  # Derived class
    def sound(self):  # Overriding method
        print("Dog barks")

# Usage
a = Animal()
a.sound()   # Output: Animal makes a sound

d = Dog()
d.sound()   # Output: Dog barks
