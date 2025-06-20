# 58.Create Car class using __init__ and __str__.

class Car:
    def __init__(self, make, model, year):
        self.make = make      # e.g., Toyota
        self.model = model    # e.g., Corolla
        self.year = year      # e.g., 2022

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"

# Example usage
car1 = Car("Toyota", "Corolla", 2022)
print(car1)
