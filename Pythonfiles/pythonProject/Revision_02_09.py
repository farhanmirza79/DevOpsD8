#STRINGS
#string1 = "hello" , 'hello' , """hello""" , '''hello''' (enclosed in either single quotes ('') or double quotes (“”)or triple quotes(""")
#strings are immutable
#strings are sequences, ordered collections

my_name = "Farhan"
          #012345

my_name = "Mirza"
print(my_name)

#Strings can be sliced
my_name = "Farhan"
          #012345
print(my_name[3])

#Slicing concepts
print(my_name[2:5]) #2,3,4,5
print(my_name[:6])  #0,1,2,3,4,5
print(my_name[3:])  #3,4,5,
print(my_name[:])

#Variables are in paranthesis(Brackets) - () , # indexes in [0,0] in square brackets

#Step slicing
print(my_name[::3]) #0,2,4,5
print(my_name[::2])
print(my_name[::-2])

#Reverse a string
city = "Atlanta"
print(city[::-1])

#Negative slicing
city = "Atlanta" # slicing always moves from left to right
       #0123456
       #-6-5-4-3-2-1
print(city[-7:-1])
print(city[-7:])



print("****************************************************************************************************")

#LISTS
# lists are sequences
# lists are mutable
# [] - Represented by square brackets []

l = [1,2,3,4]
print(type(l))

#Mutability
l = ["Mirza", 123, 8.9, [1,2,3], {"a": 1, "b":2}]
   #   0    , 1  ,  2 ,    3   ,        4
print(type(l))
print(id(l)) # memory address of l
l[0] = "Farhan"
print(l)
print(id(l))

#Slicing
l = ["Mirza", 123, 8.9, [1,2,3], {"a": 1, "b":2}]
print(l[0:3])
print(l[::2])
print(l[-1:-4])

#Built-ins
# insert
l = ["abdul", 123, 8.9, [1,2,3], {"a":1, "b":2}]
print(l.insert(1,1000))
print(l)

# Extend
l = ['a', 'b', 'c', 'd']
l1 = ['f', 'g','h', 'i']
l.extend(l1)
print(l)

# Append
l = [1,2,3]
l.append(4) # Built-in method to add elements to a existing list object
print(l)
l.append("farhan")
print(l)

# Pop method
l = [1,2,3]
l.pop() # will remove the last element fromt the list
print(l) #[1,2]
print(l) #[1,2]
l.pop(0) # will remove the element form the given index
print(1) #[2]

# Reverse a list
l = [1,2,3,4,5,-1,-2,-3]
l.reverse()
print(l)

#count method - to give a count of elements in the given list
l = [1,1,2,2,3,3,]
print(l.count(2)) #2 - since 2 is occuring 2 times in a list

#Insert - inserts an element at given index position
my_list = [1,2,3]
          # 0 1 2
my_list.insert(1,'a') # [1,'a',2,3]
print(my_list)

#remove - remove an element from the list
my_list = ["a", "b", "c","d"]
my_list.remove("d")
print(my_list)

#sort method
my_list = [1,4,7,2,9,0]
my_list.sort() # ASC order  - lower to higher
print(my_list)

my_list.sort(reverse=True) #Desc order - Higher to lower
print(my_list)

#What is the difference between shallow copy and deep copy?
# Shallow copy

l1 = [1,2,3,4,5]
l2 = l1.copy() #Shallow
l1[0] = 100
print(l1)
print(l2)

l1 = [[1,2,3],[4,5,6],[7,8,9]]
l2 = l1.copy()
print(l2)

l1[0][0] = 100 # changing in l1 will reflect in l2 as well because of shallow copy
               # as shallow,copy refers to the same object as original list
print(l1)
print(l2)

# Deep copy
import copy
l1 = [1,2,3,4,5]
l1 = copy.deepcopy(l1)
print(l1)
print(l2)

print("****************************************************************************************************")

# Tuples
# () Represented in brackets
# Tuples are sequences
# Immutable

t = ('a', 'b', 'c', 'd')
   #  0    1    2    3
t = ([1,2,3], {'a':1, 'b':2}, 123, "mirza", 7.9, False)
     #0 1 3 - index of list
     #  0           1          2      3      4      5
print(id(t))
print(t[0].append(100))
print(t)
print(id(t))
#Immutable

#Built-ins
print(t.index("mirza"))



print("****************************************************************************************************")

#Dictionaries
#Dictionaries are maps, unordered collections
#key: value pairsionaries are maps, unordered collections
#key: value pairs
#{key:value, key1:value1, key2:value2}
#Mutable

dict = {"a":1, "b":2, "c":3}
print(dict["c"])
print(id(dict))
dict["d"] = 4
print(dict)
print(id(dict))

#Keys cannot be mutable objects - it has to be immutable object
#Value can be any data type , mutable , immutable
#int, float, tuple , strins - immutable objects

d = {(1,2,3):"list1" , (4,5,6):"list2"}

#built-ins
d = {"a":[1,2,3,4], "b":{"farhan":"firstname","mirza":"lastname"}}
print(d.keys())
print(type(d))
print(d.values())
print(d.items())
#print(d.pop("a"))
print(d.get("a"))
print(d["a"])

# copy
d2 = d.copy()
print(d2)


print("****************************************************************************************************")

#Sets - are unordered collection of UNIQUE elements
#Sets are also represented by {} - Curly brackets
#Its not a map, no key:value pairs
#Sets are nothing but dictionaries but just keys
#Not a sequence

s = {1,2,3,4}
s = {(1,2,3,4), "farhan", "mirza", 5,7,9}
print(s)


l = [1,2,3,4,5,5,6,6,7,7,7,8,8,8,9,9,9,0,0,0,0,0]
s = set(l)
print(s)
l = list(s)
print(l)

l = [1,2,3,4,5]

print(l[0])
print(l[1])
print(l[2])
print(l[3])
print(l[4])


for num in l:
    print(num)















