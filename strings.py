# Strings (immutable - elements cannot be changed)
name = "bob " + 'marley'

# length of Strings
print("Length of string is: {}".format(len(name)))

# Slicing [start_index:End_index(excluding end value):Step]
print(name[0:3]) # bob
print(name[-1:-7:-1]) # yelram

""" :::::::::: Indexing Explained ::::::::::
+---+---+---+---+---+---+---+---+---+---+---+---+
| P | y | t | h | o | n |   | S | t | r | i | n |
+---+---+---+---+---+---+---+---+---+---+---+---+
  0   1   2   3   4   5   6   7   8   9   10  11
-12  -11  -10 -9  -8  -7  -6  -5  -4  -3  -2  -1
"""

# Special characters > (\n newline), (\<char> \"'etc.)

# Split() method for breaking string into a list of elements
new_name = name.split()
print("Splitted string :" + str(new_name))
