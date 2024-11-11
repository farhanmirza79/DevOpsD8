# Exception handling - try except finally blocks
# It basically handles the error that occurs during the execution of the program.
# Except blocl will be executed when an error occurs in the try block.
l = {"a":5, "b": 10 , "c": 15}
try:
    print(l["d"]) # key error
    print("This is inside try block")
except Exception as e:
    l["d"] = 20
    print("This is inside except block")
print(l)


a = 2
b = 0
try:
    print(a / b) # ZeroDivisionError
except Exception as e:
    b = 2
    print(a / b)

l = ["a", "b", "c", "d", "e", "f", 5]
try:
    for char in l:
        print(char + "ppp") # TypeError when char is 5
except Exception as e:
    print(str(char)+"ppp")

#Finally block
# Finally block is always gets executed irrespective of exception occurs or not.
l = [1,2,3,4,5,6]
try:
    print(l[2]) # index error
except Exception as e:
    l.append(7)
    l.append(8)
    print(l)
finally:
    print("This is finally block")

#Multiple Exception Blocks
l = [1,2,3,4,5,6]
try:
    print(l[1]) # IndexError
    print(l["a"]) # TypeError
except IndexError as e:
    print("IndexError occured")
except TypeError as e:
    print("TypeError occured")

