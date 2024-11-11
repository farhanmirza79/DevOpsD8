#list_num = [1,2,3,4,5,6,7,8] - Given list
#list_squared_nums = [1,4,9,16,25,36,49,64] - Expected output

#you have been given a list of integers
#Expectation is to create another list with the squares of the numbers from the given list

list_num = [1,2,3,4,5,6,7,8]

#Initialize an output list

list_sq_num = []

#iterate over teh given list and calculate square of each number and appen to the initialized list

for num in list_num:

    list_sq_num.append(num ** 2) #[1,4,9,16,25,36,49,64]
print(list_sq_num)

#Given list
list_num = [1,2,3,4,5,6,7,8,9,10]
#Expecation is for each number, if the number is odd , it should print the number and "odd"
# if the number is even, it should print the number and "even"

#Iterate over the given list,check if each number when divided by 2
#if the remainder is 0, if true,print even; if false , print odd

for num in list_num:
    if num % 2 ==0: # if 3 % 2 ==0 -> False
        print(f"{num} is even")
    else:
        print(f"{num} is odd")


#list_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#Expectation = [3, 4, 5, 6, 7, 8, 9, 10, 11, 13] Add 2 to each number from original list and append to the output list

list_num = [1,2,3,4,5,6,7,8,9,10]
list_num_2 = []
for num in list_num:
    list_num_2.append(num + 2)
print(list_num_2)


#Nested list, Nested Tuples
#Nested list with all iterable elements
nested_list = [[1,2,3],[4,5,6],[7,8,9]]
for main_list in nested_list:
    for num in main_list:
        print(num)

#Nested list but with one or more element as a non-iterable element
nested_list = [[1,2,3],[4,5,6],7]
for sub_list in nested_list:
    if isinstance(sub_list,list): # [1,2,3],[4,5,6] # we are checking if sub_list is a list data type,only then are iterating
        for num in sub_list:
            print(num)
    else:
        print(sub_list)

nested_list = [[1,2,3],[4,5,6], ("a", "b", "c"),7]
for sub_list in nested_list:
    if isinstance(sub_list,(list,tuple)): ## we are checking if sub_list is a list data type,only then are iterating
        for num in sub_list:
            print(num)
    else:
        print(sub_list)

#Flattening list #(Most asked Interview question)

list_num = [1,2,3,4,5,[6,7,8],(9,10,11), 12,13]
#Expected output = [1,2,3,4,5,6,7,8,9,10,11,12,13]

# initialize output list
flatten_list = []
for num in list_num: #num - [6,7,8]
    if isinstance(num,(list,tuple)):
        flatten_list.extend(num)
    else:
        flatten_list.append(num)
        print(flatten_list)
print("****************************************************************************************************")

#Iterate over the list and print each element, modify the above program to do so

dict_1 = {"a": 1, "b": 2, "c": [3,4,5,6]}


for key,value in dict_1.items():
    print(key)
    print(value)
iterate_list = dict_1["c"]
for integers in iterate_list:
    print(iterate_list[:])

print("****************************************************************************************************")

print("Dictionary iteration")
dict_1 = {"a":1, "b":2, "c": [3,4,5,6]}
for key,value in dict_1.items(): # 3rd iteration - key is c , value is [3,4,5,6]
    if isinstance(value, list):  # 3rd iteration -> value = [3,4,5,6] -> is a list, hence true
        print(key)
        for num in value:
            print(num)
    else:
        print(key)
        print(value)

print("****************************************************************************************************")

#Iteration using range()
print ("Iteration using range function")
list_name = [1,2,3,4,5,6,7,8]
            #0 1 2 3 4 5 6 7
for i in range(0, len(list_num)): #range (0,8) -> 0,1,2,3,4,5,6,7
    print(list_num[i]) # list_nums[1]

print("****************************************************************************************************")

list_nums = [2,4,3,7,9,8,-2,11,-4,5]
#Question , if sum of any two numbers from the list ==7, -> print indexes of any two such numbers
for i in range(0, len(list_nums)):
    for j in range(i+1, len(list_nums)):
        if list_nums[i]+list_nums[j] ==7:
            print((i,j)) #(0,9)

print("****************************************************************************************************")

list_nums = [2,4,3,7,9,8,-2,11,-4,5]
            #0 1 2 3 4 5  6  7  8 9
# #Question is find the greatest number from the list and its index
greatest_number = list_nums[0] #assumption 2

for i in range(0, len(list_nums)): #i=3
    if list_nums[i] > greatest_number: # list_nums[3]
        greatest_number = list_nums[i] #7
        index_greatest_number = i #1
print(f"Greatest number is {greatest_number}, index of greatest number is {index_greatest_number}")

print("****************************************************************************************************")
