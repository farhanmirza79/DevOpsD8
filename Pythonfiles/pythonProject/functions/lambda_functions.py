#Interview Questions
#lamda functions are anonymous funcitions that are defined using the lambda keyword.
#Small operations that can be defined in a single line
def add_nums(a, b):
    return a + b

l = lambda a, b : a + b
print(l) # l is function pointing towards lambda function address in memory
print(l(5,10))

def sq_num(num):
    return num **2

f = lambda num: num ** 2
print(f(5))

#Write a lambda function to check if a number is even

def check_even(num):
    if num % 2 == 0: # True or False
        return True
    else:
        return False

f = lambda num: num % 2 == 0
print(f(13))


def even_num(num):
    return num % 2 == 0
f = lambda num: num % 2
print(f(2))

#Write a lambda function that should return the sum of 3 numbers
def sum_of_nums(a,b,c):
    return a + b + c
f = lambda a, b, c : a + b + c
print(f(1,2,3))

# Maps & Filters in lambda functions
# Map applies a function to all the items in an input list
def sq_num(list_nums):
    output_list = []
    for n in list_nums:
        output_list.append(n ** 2)
        return output_list
sq_num_list = sq_num([1,2,3,4,5])
print(sq_num_list)

#Using Map function
l = [1,2,3,4,5]
f = list(map(lambda n:n ** 2))
print(f)


l = ["a", "b", "c", "d", "e", "f"]
def upper_case_list(list_chars): #'''function takes a list of characters and return the uppercase of each character in the given list'''
    output_list = []
    for char in list_chars:
        output_list.append(char.upper())
        return output_list

l = upper_case_list(["a", "b", "c", "d", "e", "f"])
print(l)
# Using Map function
# Map function applies a given function to every element in a given list
l = ["a", "b", "c", "d", "e", "f"]
f = list(map(lambda c: c.upper(),l))
print(f)

#Filter function
#Filter function filters the given list based on the condition given in the lambda function

l = [1,2,3,4,5,6]
def check_even(list_num):
    output_list = []
    for num in list_num:
        if num % 2 == 0:
            output_list.append(num)
    return output_list
l = check_even([1,2,3,4,5,6])
print(l)

# Using filter function
l = [1,2,3,4,5,6]
f = list(filter(lambda n: n % 2 == 0,l))
print(f)

list_strings = ["abdul", "mateen", "abc","ff", "l"]
def filtered_strings(list_strs):
    output_list = []
    for s in list_strs:
        if len(s) > 2:
            output_list.append(s)
    return output_list

l = filtered_strings(["abdul", "mateen" , "abc", "ff", "l"])
print(l)

list_strs = ["abdul", "mateen" , "abc", "ff", "l"]
list_filtered_strs = list(filter(lambda s: len(s) >2, list_strs))
print(list_filtered_strs)

list_filtered_upper = list(filter(lambda s: s[0].isupper(), list_strs))
print(list_filtered_upper)