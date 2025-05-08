# 39.Tuple unpacking and swapping values using tuples.

# Basic tuple unpacking
person = ("Alice", 25, "Engineer")

name, age, profession = person

print(name)       # Alice
print(age)        # 25
print(profession) # Engineer

# swapping
x = 10
y = 20

x, y = y, x

print(x)  # 20
print(y)  # 10
