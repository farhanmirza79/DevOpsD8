#Concantenation  # 21 AUG
first_name = "Mateen"
last_name = "Mohammed"
print(first_name+" "+ last_name)

age = 28.5
print(type(age))

str_age = str(age) #Type casting - int age changed to str age
print(type(str_age))

print("My age is " + str(age))

age = 25
ID = 14177
salary = 10_1000
name = "Mateen"
statement = "My name is "+name+" . My Emp ID is "+str(ID)+"My Salary is "+str(salary)
print(statement)

print("*********************************************************************")

#format method

statement = ("My name is {}. My Emp ID is {}. My age is {}. My salary is {}. My name is {}"
             .format(name,ID,age,salary,name))
print(statement)

statement = ("My name is {0}. My Emp ID is {1}. My age is {2}. My salary is {3}. My name is {0}"
             .format(name,ID,age,salary))

print("*********************************************************************")

#f-strings - formatted strings

statement = f"My name is {name}. My Emp ID is {ID}. My age is {age}. My salary is {salary}."
print(statement)

print("*********************************************************************")

#22 AUG

#\n - new ling (#To print in a new line)
statement = f"My name is {name}.\n\nMy Emp ID is {ID}.\n\nMy age is {age}.\n\nMy salary is {salary}.\n\n"
print(statement)

print("*********************************************************************")

#\t - tab (#to represent a horizontal tab,
      # It is often used to create indentation in text or to format output in a table-like structure)

print("*********************************************************************")

table_headers = "name\t\t age \t\t email \t\t phone"
print(table_headers)

#\\ - backslashes used for writing paths of folders/files in linus environment
my_file_path = " \\users\\downloads\\myfolder\\notes"
print(my_file_path)

print("*********************************************************************")


 #\' or \"
statement = "Hello, very good morning. What a \"Wonderful\" day!!"
print(statement)
statement = 'Hello, very good morning. What a "Wonderful" day!!'
print (statement)

statement = 'Hello, very good morning. What a \'Wonderful\' day!!'
print(statement)
statement = "Hello, very good morning. What a \'Wonderful\' day!!"
print(statement)

Statement = f"""My name is {name}.
My Emp ID is {ID}.
My age is {age}.
My 'salary is {salary}."""
print(statement)


a = 42
b = 2

if (a % b) ==0:
    print(f"{a} is even")
else:
    print(f"{a} is odd")

a = 31
b = 2

if a % b == 0:
    print(f"{a} is even")
else:
    print(f"{a} is odd")


print("*********************************************************")
# Question 1
list_of_numbers = ["10","20","30","40","50","60","70","80","90","100"]
print(list_of_numbers[:5])
print(list_of_numbers[5:])
print(list_of_numbers[::2])
print(list_of_numbers[1::3])
print(list_of_numbers[::-1])

print("*********************************************************")
# Question 2
a = 1
if a <=1:
    print("The number is not prime")
if a == 6:
    print("The number is prime")


print("*********************************************************")

# Question 3

first_name = "Farhan"
last_name = "Mirza"
age = 29

greeting_message = f"Hello, {first_name} {last_name}! You are {age} years old."

print(greeting_message)


