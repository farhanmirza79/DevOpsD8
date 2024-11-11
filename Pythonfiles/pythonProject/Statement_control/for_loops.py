#For loop - iteration mechanism
#A for loop interates over an interable.


string_name = "Mateen"
for char in string_name:
    print(char)
    print("iteration is going on")

print("iteration completed")


print("List for loop execution")
list_random = ("abdul", "mateen",7,8.99, [1,2,3], (7,8,9), {"a":1, "b":2}) #Iterable
for data in list_random:
    print(data)

print("tuple for loop execution")
tuple_random = ("abdul", "mateen",7,8.99, [1,2,3], (7,8,9), {"a":1, "b":2}) #Iteration
for data in list_random:
    print(data)

#Convert the strings in given list to uppercase
list_names = ["abdul", "mateen", "abuzar", "mubeen", "farhan", "amair"]
for name in list_names:
    print(name.upper())

print("****************************************************************************")

#Print the first character of each string from the given list of strings
list_names = ["abdul", "mateen", "abuzar", "mubeen", "farhan", "amair"]

for name in list_names:
    print(name[0])


dict_1 = {"a":1, "b":2, "c":3}

for k,v in dict_1.items(): #iterate over key, value pairs
    print(k)
    print(v)

for k in dict_1.keys(): #iterate only over keys
    print(k)

for v in dict_1.values(): # iterate only over values
    print(v)

print("****************************************************************************************************")
dict_1 = {"a": 1, "b": 2, "c": [3,4,5,6]}
for key, value in dict_1.items(): #3rd Iteration - key is c, value is [3,4,5,6]
    if isinstance(value, list):# 3rd iteration -> value = [3,4,5,6] -> is a list, hence true
        print(key)
        for num in value: #[3,4,5,6]
            print(num)
    else:
        print(key)
        print(value)

print("****************************************************************************************************")

input_dict ={"a": 1, "b": 2, "c": 3.5, "d": "mateen"}

def dict_1 (input_dict):
    output_dict = {}
    for key, value in input_dict.items():
        if isinstance(value, (int, float)):
            output_dict[key] = value + 2
        else:
            output_dict[key] = value
    return output_dict

print("****************************************************************************************************")

