a = 5
b = 5
c =5

#Comaparison Operators -> Yield Boolenans Values - True or False
print(a ==b)# will compare the vaule of the variable - Object
print(a is b)# it will check if both a and b vaules reside in the same memory location
print(id(a), id(b))

a = [1,2,3]
b = [1,2,3]
print(a == b)
print(a is b)

print("********************************")
#Not equal to
num1 = 100
num2 = 200
print(num1 != num2)

print("********************************")
#Greater than and greater than and equal to
num1 = 100
num2 = 200
print(num1 > num2) #100 > 200 -> False
print(num1 >= num2)

print("********************************")
#Lesser than and lesser than or equal to
num1 = 100
num2 = 200
print(num1 < num2)
print(num1 <= num2)