list_nums = [1,2,3,4,5]
#list_sq_num = [1,4,9,16,25]
#Conventional method
list_sq_num = []
for num in list_nums:
    list_sq_num.append(num ** 2)
print(list_sq_num)

#list comprehension
list_nums = [1,2,3,4,5]
list_sq_num_comp = [num ** 2 for num in list_nums]
print(list_sq_num_comp)

print("****************************************************************************************************")

string = "Python is an awesome language"
list_of_strings = string.split(" ") #['python', 'is', 'an', 'awesome', 'language']
#filtered_list = [['python', 'awesome', 'language']
print(list_of_strings)



#Conventional method
filtered_list = []
for word in list_of_strings:
    if len(word) >=5:
        filtered_list.append(word)
print(filtered_list)

#Comprehension method
filtered_list_comp = [word for word in list_of_strings if len(word) >=5]

#Dictionary comprehensions
list_nums = [1,2,3,4,5]
#output_dict = {1: 1,2: 4,3: 9,4: 16, 5: 25}



#Conventional method
output_sq_dict = {}
for num in list_nums:
    output_sq_dict[num] = num ** 2 #add key value pair to dictionary
print(output_sq_dict)


#Dictionary comprehensions
list_nums = [1,2,3,4,5]
output_sq_dict_comp = {k: k ** 2 for k in list_nums}
print(output_sq_dict_comp)


strings = "aaabbbcccdddeeef"
#{a: 3, b: 3, c: 3, d: 3, e: 3}
char_count = {} #{'a: 3, 'b': 3, 'c':3}
for char in strings:
    if char in char_count.keys():
        char_count[char] = char_count[char] + 1 #char_count['c']
    else:
        char_count[char] = 1 #output_dict_char_count['c'] = 1
print(char_count)

print("*******************************************************************************************")
#Practice

list_nums = [1,2,3,4,5]
#list_sq_nums = [1,4,9,16,25]

list_sq_num = []

for nums in list_nums:
    list_sq_num.append(nums ** 2)

print(list_sq_num)

list_nums = [1,2,3,4,5]
#list_even_nums = [2,4]
list_even_nums = []

for num in list_nums:
    if num % 2 == 0:
        list_even_nums.append(num)

print(list_even_nums)



