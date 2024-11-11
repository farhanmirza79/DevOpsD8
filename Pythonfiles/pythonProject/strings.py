random_var = ("a1b1c1")

print(type(random_var))

my_first_name = "Mohammed"
my_second_name = "Mateen"
print("*******************************************************")
my_age = 25
my_newage = my_age +10
print(my_newage)

print("***************************") # 20 Aug
#strings are immutable
my_name = "Abdulmateen"
my_name = "Abdulkareem"
          #012345678910
          #......-3-2-1
print(type(my_name))
#my_name[10] = "m"
print(my_name[5])# You can access elements using their positional index
print(my_name[8])
#print(my_name[11]) # This will through indererror
print(my_name[-1]) # Negative indexing

print("*******************************************************")

#methods
#methods are called by dot (.) notation - Python built-ins
my_name = " AbdulKareem "
print(my_name.capitalize()) # it will capitalize the first letter
print(my_name.upper()) # it will change the entire to uppercase
print(my_name.lower()) # it will change the entire to lowercase
print(my_name.strip()) # it will strip the preceding and succeeding spaces from the strip
print(my_name.lstrip()) # it will strip only the preceding space
print(my_name.rstrip()) # it will strip only the succeeding space

print("*******************************************************")

my_string = "--helloworld--"
print(my_string.strip("-")) # it will strip based on the character and based to the strip method

text = "hello world" # "hello there"
print(text.replace("world","there"))


text = "Hello-world"
print(text.split("-"))

print(text.startswith("H"))
print(text.endswith("e"))

print(text.isupper()) # Will check if string is completely in upper case - returns bool - True or False
print(text.islower()) # Will check if string is completely in lower case - returns bool - True or False

age = ('1a2b3c')
print(age.isnumeric()) # will check if the string value is completely numerical - return boolean - true or false
print(age.isalnum()) # will check if it is alpha-numeric - returns bool - True or false

# To calculate the length of the string
city = "hyderabad"
       #012345678
print(len(city))

