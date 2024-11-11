#Sets are unordered collection of UNIQUE elements - #Represented by {} curly braces
#Sets are mutable
#Sets can only store immutable elements

s = {1,2,3,4,4}
print(type(s))
print(s) # Remove the duplicate elements automatically if its repeated

#built-ins
s.add(100)
print(s)
s.remove(100)
print(s)

s1 = {1,2,3,8}
s2 = {4,5,6,8}

#Set Union - will merge the given inputs in a set

print(s1.union(s2))
print(s1 | s2) # other representation of Union "|"
#Set intersection - will take common elements as output in sets

print(s1.intersection(s2))
print(s1 & s2)

s = set()
s.add(1)
s.add(2)
s.add(3)
print(s)

#Interview questions
l = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,5,5,6,7]
s = set(l)
print(list(s))

#Booleans
a = True
b = False

print(type(a),type(b))

