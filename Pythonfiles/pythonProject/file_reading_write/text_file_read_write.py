#Open file in read mode
#Open returns a file object, which has a read method for reading the content of the file
file = open("example.txt") # Returns a file object
content = file.read()
print(content)
file.close() # close the file after reading the content

#With statement opens the file, does the operations and close the file
with open("example.txt", 'r') as file:
    content = file.read() # stores the content as a string
    print(content)
    print(type(content))

with open("example.txt", 'r') as file:
    for line in file: # reads the file line by line
        print(line.strip())

with open("example.txt", 'r') as file:
    lines = file.readlines() # stores the content as a list of string
    print(lines)
    print(type(line))

print("*********************eExpection handling*******************")
try:
    with open("test.txt, 'r") as file:
        lines = file.readlines() # Stores the content as a list of stirngs
        print(lines)
        print(type(lines))
except FileNotFoundError as e:
    print("File not found")
except Exception as e:
    print("Some error occured")

#Write mode
with open("test.txt", 'w') as file:
    file.write("This is a test file")


# Write mode will overwrite the content of the file

with open("example.txt", 'r') as infile, open("test.txt, 'w") as outfile:
    for line in infile:
        outfile.write(line)

# This is append mode with which will append the content to the file
with open ("test.txt", 'a') as file:
    file.write("\nThis is a test file")
