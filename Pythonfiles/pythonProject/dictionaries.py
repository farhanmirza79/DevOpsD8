#Dictioinaries are maps - not sequences - Represented by {} - Curly braces
# keys : value pairs
# Keys must be an immutable object
# values can be any data type
# Don't use duplicates key's
# Keys cannot be null
# Dictionaries are also mutable objects
# Dictionaries are unordered by default
# python 3.6 - They have made it ordered
d = {"firstname": "abdul mateen", "lastname":"mohammed"}
d = {1:"one", 2:"two", 3: "three", 1: "ONE"}


d = {
    (0,0): "origin",
    (1,1): "Q1",
    (-1,1):"Q2"
}
print(d[(0,0)])

d = {"apple": ["phones", "airpods", "macbooks", "smartwatches"], "samsung": ["phones", "earpods", "notebooks", "smartwatches"]}
print(d["apple"][1])

d = {"apple": {"iphones": {"phone1": "iphone15", "phone2" : "iphone16", "phone3": "iphone17"}}}
print(d["apple"]["iphones"]["phone2"])

d = {"firstname": "abdul mateen", "lastname": "mohammed"}
#I want to add a new value pair
d["fullname"] = "mohammed abdul mateen"
print(d)

#change a value fora specific key
d["lastname"] = "shaikh"
print(d)

del d["fullname"]
print(d)

#built-ins of dictionaries
d = {"firstname": "abdul mateen", "lastname": "mohammed"}
print(d.keys())  #Fetch only keys in list of tuple format
print(d.values())  #Fetch only value in list of tuples format
print(d.items())  # Fetch keys and values in list of tuples format
print(d.get("firstname")) #Fetch a value for a particular key

# COPY
d2 = d.copy() # copy a dict
print(d2)

#CLEAR
d.clear() #remove all the key value pairs in a dict
print(d)

#POP
d = {"firstname": "abdul mateen", "lastname": "mohammed"}
d.pop("firstname") # Remove a specific key value pair
print(d)

d = {"firstname": "abdul mateen", "lastname": "mohammed"}
d1 = {"footballer":"ronaldo"}

d.update(d1) #add one dictionary to another
print(d)

d = dict() # {} # contructor
d[1] = "apple"
d[2] = "samsung"
d[3] = "nokia"

print(d)

