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


# Safely look up a key that might be missing with get().
server = {
    'name': 'web-01',
    'status': 'ACTIVE'
}

# get() returns the value when the key exists.
status = server.get('status')
print(status)  # ACTIVE

# get() returns None when the key does not exist.
build_status = server.get('build_status')
print(build_status)  # None

# A second argument provides a different default value for a missing key.
build_status = server.get('build_status', 'UNKNOWN')
print(build_status)  # UNKNOWN

# Unlike get(), square brackets raise KeyError if the key is missing:
# build_status = server['build_status']

# Use "in" when you need to distinguish between a missing key and a key
# whose value is actually None.
if 'status' in server:
    print('The status key exists.')
