# Range function - its a built-in python function that we can use to create ranges of integer values
# The return value is not a list or a tuple, it is a special range object:
# Integers between certain range

list_1 = [1,2,3,4,5,6,7,8,9,10] # creates a placeholder for list object and stores all the elements
my_numbers = range(0,10) # 0-9 n-1 # memory efficent than list # only cretes a range object
print(my_numbers)

list1 = list(my_numbers) # can convert range object to a list
print(list1)

list2 = [1,2,3,4,5,6,7,8,9,10]
numbers = range(0,10,2)
print(list(numbers))

tuple_1 = tuple(numbers) # can convert range object to a range
print(tuple_1)

my_numbers = range(10,100)
my_numbers = range(0,10,2)
print(list(my_numbers))
print(type(my_numbers))

