# list_num = [1,2,3,4,5,6,7,8]
# list_squared_nums = [1,4,9,16,25,36,49,64]

# You have been given a list of integers
# Expectation is to create a another list with the squares of the numbers in the given list

list_num = [1,2,3,4,5,6,7,8,9]

# Initialize an output list

list_sq_num = []

#Iterate over the given list and calculate square of each number and append to the initialized list
for num in list_num:
    sq_num = num ** 2
    list_sq_num.append(sq_num)
print(list_sq_num)


print("****************************************")
for num in list_num:
    list_sq_num.append(num ** 2)
print(list_sq_num)


# Given list
list_num = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]

#Expected output is for each number, if the number is odd , it should print the number and "odd"
#if the number is even , it should print the number is "even"

for num in list_num:
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num}is odd")

print("****************************************")

#list_num = [1,2,3,4,5,6,7,8,9,10]
#Expected output = [3,5,6,7,9,10,11,12]

list_num = [1,2,3,4,5,6,7,8,9,10]
added_num = []
for num in list_num:
    added_num.append(num+2)

print(added_num)

#Nested list , Nested tuple

nested_list = [[1,2,3],[4,5,6],[7,8,9]]

for each_list in nested_list:
    for num in each_list:
        print(num)


nested_list = [[1,2,3],[4,5,6],7]

for sub_list in nested_list:
    if isinstance(sub_list,list):
        for num in sub_list:
            print(num)
    else:
        print(sub_list)