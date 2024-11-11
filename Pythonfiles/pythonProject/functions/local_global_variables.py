age = 28 # Global space -> the scope of this variable is global, can be used inside the function and outside the function
def print_my_name():
    first_name = "mateen" # local space -> The scope of this variable is local, can be called only inside the function
    last_name = "Mohammed"
    full_name = first_name + last_name
    print(f"my name is {full_name} and age is {age}")
    print(locals()) # To view local space variables

print(globals()) # To view global space variables

print_my_name()
print(age)

def calculate_sq_list(list_nums): # [1,2,3,4] [1,4,9,16]
    sq_list = []
    for num in list_nums:
        sq_list.append(num ** 2)
    return sq_list # [1,4,9,16] # Return list value

def calculate_add_2(sq_list): #[1,4,9,16]
    added_list = []
    for num in sq_list:
        added_list.append(num + 2)
    print(added_list) # [3,6,11,28]

list_squared = calculate_sq_list([1,2,3,4,]) # [1,4,9,16]
calculate_add_2(list_squared) # passed returned value from one function to another function

def calculate_sq_num(a, b, c):
    sq_a = a ** 2
    sq_b = a ** 2
    sq_c = a ** 2
    return sq_a, sq_b, sq_c # Return multiple variable/values form a function

sq_val_a, sq_val_b, sq_val_c = calculate_sq_num(1,2,3)
print(sq_val_a,sq_val_b,sq_val_c)

def check_even(num):
    if num % 2 == 0:
        return True # Return bool value based on conditionals
    else:
        return False
bool_val = check_even(5)
print(bool_val)

#Default parameters/arguements
def calculate_sum_numbers(a,b,c,d,e=0): #Default parameter
    return a + b + c + d + e

sum_vars = calculate_sum_numbers(2,3,4,5,10)
print(sum_vars)


def build_dictionary(dict={}) : #Default parameters
    dict['a'] = 1
    dict['b'] = 2
    dict['c'] = 3
    return dict

returned_dict = build_dictionary({'d': 4, 'e':5})
print(returned_dict)


##You have to write a function that takes a dictionary as an input parameter
#a new dictionary where the key is the key from given dictionary,
# the value is value if its a string, or if its int or float, the value is value + 2

{"a": 1, "b": 2, "c": 3.5, "d": "mateen"} #Given input dict
{"a": 3, "b": 4, "c": 5.5, "d": "mateen"} #output dictionary







