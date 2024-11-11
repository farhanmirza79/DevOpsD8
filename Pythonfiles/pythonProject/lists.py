list_of_names = ["mateen", "Mohammed", "talha", "amair ", "abuzar", "messi"]
                #     0        1         2        3           4         5
                #    -6        -5        -4        -3         -2        -1
list_of_random_data = ["Apple", 13,17.0]
#lists are heterogenous
#lists are mutable
#lists are also sequences

print(list_of_names[2])
list_of_names[2] = "Rolando" #Item assignment - proves mutability
print(list_of_names)
print(list_of_names[4])
print(list_of_names[-1])

#slicing ['mateen' , 'Ronaldo' , 'abuzar']
print(list_of_names[:3])

#step slicing
print(list_of_names[::2])


#reverse a list
list_of_names = ["mateen", "mohammed", "talha", "amair", "abuzar", "messi"]
print(list_of_names[::-1])


#Apple - p, Samsung - s, Blackberyy - b, Google - g, Nokia - a
list_of_phones = ["Apple", "Samsung", "Blackberry", "Google", "Nokia"]
print(list_of_phones[0][2])
print(list_of_phones[2][5])
print(list_of_phones[4][4])
print(list_of_phones[1][3])
print(list_of_phones[3][3])
print(list_of_phones[4][2])

print(list_of_phones[-5][-3]) #Negative indexing
print(list_of_phones[-3][-5])

#28 AUG

#Nested list
lists_nested = [1,2,3,[4,5,6]]
list_nested1 = [["mateen", "abuzar"],[45,67],10,12]
print(list_nested1[1][1])
print(list_nested1[0][0][3])

list_random_data = [["Apple",["Iphone", "Airpods", "Macbook pro M3",]],["Samsung", ["S24 Ultra","Earpods", "Tab"]]]
print(list_random_data[0][1][1])
print(list_random_data[1][1][2])

#list built-ins

#Mutable objects

#Append Method
l = [1,2,3]
l.append(4) #Built-in method to add elements to a existing list object
print(l)
l.append("mateen")
print(l)

#Pop method
l = [1,2,3]
l.pop() # Will remove the last element from the list
print(l) # [1,2]
print(l) # [1,2]
l.pop(0) # Will remove the element from the given index
print(1) #[2]

#Reverse a list
l= [1,2,3]
l.reverse()
print(l)

#count method - To give a count of elements in the given list
l = [1,1,2,2,3,3]
print(l.count(2)) #2 - Since 2 is occuring 3 times in the list

l = ["a", "a", "a","b", "b","c","c","d"]
print(l.count("a")) # 3 - since "a" is occuring 3 times in a list

#Insert - inserts an element at given index position
my_list = [1,2,3]
          #0 1 2
my_list.insert(1,'a') # [1, 'a', 2, 3]
print(my_list)

#remove - remove an element from the list
my_list = ["a","b", "c", "d"]
my_list.remove("c")
print(my_list)

#sort - method
my_list = [1,4,7,2,9,0]
my_list.sort() # ASC order - lower to higher
print(my_list)

my_list.sort(reverse=True)
print(my_list)

#What is the difference between shallow copy and deep copy?
#Shallow copy
l1 = [1,2,3,4,5]
l2 = l1.copy() #Shallow
l1[0] = 100
print(l1)
print(l2)


l1 = [[1,2,3],[4,5,6],[7,8,9]]
l2 = l1.copy()
print(l2)

l1[0][0] = 100 # Changing in l1 will reflect in l2 as well because of shallow copy as shallow copy refers to the same object as original list
print(l1)
print(l2)



#Deep copy
import copy
l1 = [1,2,3,4,5]
l2 = copy.deepcopy(l1)
print(l1)
print(l2)

l1 = [[1,2,3], [4,5,6],[7,8,9]]
l2 = copy.deepcopy(l1)
l1[0][0] = 100 #change in l1 will not reflect in l2 as deep copy creates completlely new independent object
print(l1)
print(l2)

#Converting other sequences to lists
l = list('abcde')
print(l)

t1 = (1,2,3,4,5)
new_list = list(l1)
print(new_list)

l= list() #[] - empty list
l.append(1)
l.append(2)
l.append(3)
print(l)
