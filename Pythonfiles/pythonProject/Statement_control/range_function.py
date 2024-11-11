#Range function
#intergers between certain range

list_1 = [0,1,2,3,4,5,6,7,8,9,10] # creates a placeholder for list object and stores all the elements in memory
my_numbers = range(100) # 0-9 (n-1) # memory efficient than a list # only creates a range object, will generate ingegers on the fly
print(my_numbers)

list1 = list(my_numbers) # can convert a range object to a list
print(list1)

t1 = tuple(my_numbers) # can convert a range object to a tuple
print(t1)

my_numbers = range(10,100)#10........99 #starting or lower boundary, ending or upper boundary
my_numbers = range(0,10,3) # 0,1,2,3,4,5,6,7,8,9 # steps
print(list(my_numbers))
my_numbers = range(0,10,2)
print(list(my_numbers))





