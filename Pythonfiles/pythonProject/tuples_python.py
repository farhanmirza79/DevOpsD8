#Tuples are immutalble -
#Tuples are heterogeneous sequence

t1 = (1,2,3,4,5)
print(type(t1))
print(t1[0])

t2 = ("abdul", "mateen", 12, 9.5, [1,2,3,4,5])
t2[4].append(100) #list element inside tuple - list is mutable, tuple is not
print(t2)


#Tuple built-ins
print(t2.count("abdul"))
print(t2.index("mateen"))

#Tuple concatenation
t1 = (1,2,3,4,5)
t2 = (5,6,7,8,9)
t3 = t1 + t2
print(t3)

#Type casting - converting one sequence to another
l = [1,2,3,4,5]
t = tuple('abcde')
print(t)
