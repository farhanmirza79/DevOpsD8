# For loop - iteration mechanism
# A for loop iterates over an iterable


string_name = "Farhan" # Iterable

for char in string_name: # Iteration
    print(char)
    print("Iteration going on")
print("Iteration completed")


full_name = "Farhan Mirza Baig"

for char in full_name:
    print(char)

print("List for loop execution")

list_random = ["Farhan", "Mirza", 7, 8,9, [1,2,3], (4,5,6), {"a": 1, "b":2, "c":3}]

for data in list_random:
    print(data)

print("Tuple for loop execution")

tuple_random = ("Farhan", "Mirza", 7, 8,9, [1,2,3], (4,5,6), {"a": 1, "b":2, "c":3})

for data in tuple_random:
    print(data)


list_name = ["farhan", "mateen", "mubeen", "amair", "abuzar", "nahid", "mudassir","arshad"]

for name in list_name:
    print(name.upper())
    print(name.capitalize())

# Print the first character of each string from the given list of strings

list_names = ["farhan", "mateen", "mubeen", "amair", "abuzar", "nahid", "mudassir","arshad"]

for names in list_names:
    print(names[0])

# Dictionaries
print("*******************Dictionaries*********************")

dict_1 = {"a": 1,"b": 2, "c": 3}

for k,v in dict_1.items(): # Iterate over keys , value pairs
    print(k)
    print(v)

for k in dict_1.keys(): # Iterates only keys
    print(k)

for v in dict_1.values(): # Iterates only values
    print(v)



