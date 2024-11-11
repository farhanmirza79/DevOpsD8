num_1 = 100
num_2 = 200
print("*****************************")


#Addition
print(num_1 + num_2)
print(num_1.__add__(num_2))
print("*****************************")

#Subtraction
print(num_1 - num_2)
print("*****************************")

#Multiplication
print(num_1 * num_2)
print("*****************************")

#Division
print(num_1 / num_2)
print("*****************************")

#Exponents - powers
print(num_1 ** 2,num_1 ** 3, num_1 ** 0.50)

print("*****************************")

#Floor division - integer part of the divison rule
num_3 = 10
num_4 = 3
print(num_3 // num_4)

print("*****************************")

#modulus - remainder when divided
num_5 = 25
num_6 = 4
print(num_5 % num_6)

#Operator precedence
print(100-25+20) # PEMDAS # PEDMAS - Paranethesis, Exponents, Division/Multiplication, Addition/Subtraction
print((100-25)+20)
print(100 * 4 +4 *25)
print((100 * 4) + (4 *25))
print(10 * 2 ** 3)
