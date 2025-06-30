# 66.Sort a list of dictionaries by a value.
people = [
    {"name": "Ali", "age": 25},
    {"name": "Sara", "age": 30},
    {"name": "Zain", "age": 22}
]

# Sort by age
sorted_people = sorted(people, key=lambda x: x["age"])

print(sorted_people)
