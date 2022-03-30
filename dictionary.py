# Keys and values of Dictionaries
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 25,
    'favorite_colors': ['blue', 'green'],
    'active': True
}

# items(), keys(), values()
for item in person.items():
    print(item)

for key in person.keys():
    print(key)

for value in person.values():
    print(value)
