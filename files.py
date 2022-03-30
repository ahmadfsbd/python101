# Open file for reading
with open('readme.txt') as f:
    lines = f.readlines()
    print(lines)
    f.close()

# or
with open('readme.txt', 'r') as file:
    lines = []
    for line in file:
        lines.append(line.rstrip('\n'))
    print(lines)

"""
open(path_to_file, mode)
Mode	Description
'r'	Open for text file for reading text
'w'	Open a text file for writing text
'a'	Open a text file for appending text

read() – read all text from a file into a string.
readline() – read the text file line by line and return all the lines as strings.
readlines() – read all the lines of the text file and return them as a list of strings.
"""
# Write in the file
with open('readme.txt', 'a') as f:
    f.write('readme\n')
    f.close()
