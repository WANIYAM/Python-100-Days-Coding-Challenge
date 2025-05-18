# 48.Create a custom exception for age validation.

def check_age(age):
    if age < 18:
        raise Exception("You must be 18 or older.")
    print("Age is valid.")

# Example usage
try:
    age = int(input("Enter your age: "))
    check_age(age)
except Exception as e:
    print("Error:", e)
