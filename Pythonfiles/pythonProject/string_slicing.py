my_text = "Hello World!"
          #01234
print(my_text[0])
print(my_text[0:5]) #0123 # slicing - 5 is exclusivr - (n-1)
print(my_text[:5])  #Starting till 4th
print(my_text[:])   #Starting untill last
print(my_text[3:7]) #3rd index till 6th

print("*******************************************************")

#Negative slicing
city = "Hyderabadi" # slicing always moves from left to right
       #0123456789
       #-10-9...-1 # Negative indexes - Indices
print(city[-5:-1])

print("*******************************************************")

#step slicing
city = "Hyderabadi"
print(city[0:10:2])
print(city[::2]) #every second element starting from 0th index
print(city[::3]) #every third element starting from 0th index
print(city[1::3]) #Starting and ending point inclusive
print(city[-10::2]) #same as (city[0:10:2]) but using negative indexes

print("*******************************************************")

#Reverse a string - Interview question
city = "Hyderabadi"
print(city[::-1]) # prints reverse string -1 will consider steps in negative direction-from right to left
