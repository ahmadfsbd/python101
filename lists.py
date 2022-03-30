# Lists are mutable and elements can be changed/replaced
lname = ["bob", "jack", 'beth']
print(lname)

"""
Use list[index] = new_value to modify an element from a list.
Use append() to add a new element to the end of a list.
Use insert() to add a new element at a position in a list.
Use pop() to remove an element from a list and return that element.
Use remove() to remove an element from a list.
"""
# append ahmad
lname.append('ahmad')
print(lname)
# pop bob
popped = lname.pop(0)
print(lname)
print("The name {} was popped from list.".format(popped))

# sort list in place
scores = [5, 7, 4, 6, 9, 8]
scores.sort(reverse=True)
print(scores)

# Sorting based on a sort_key
companies = [('Google', 2019, 134.81),
             ('Apple', 2019, 260.2),
             ('Facebook', 2019, 70.7)]
# Create a function that returns sort_key
def sort_key(company):
    return company[2]
# Pass the function to sort() function
companies.sort(key=sort_key, reverse=True)
print(companies)

# Slicing a list (same as string slicing)
print(companies[0:2:1])

# Unpacking Lists
apple, google, facebook = companies
print("Unpacked list element google = {}".format(google))
# Assign remaining elements as new list to others variable
apple, *others = companies
print("Others List:" + str(others))

# iterate over a List
for item in companies:
    print(item)

# Find index of an element
cities = ['New York', 'Beijing', 'Cairo', 'Mumbai', 'Mexico']
city = 'Mexico'
print("index of Mexico: " + str(cities.index(city)))

for city in cities:
    result = cities.index(city)
    print(f"The {city} has an index of {result}.")

# Usin range to iterate
length = len(cities)
for i in range(0, length, 2):
    print(f"At index {i} : {cities[i]}")
