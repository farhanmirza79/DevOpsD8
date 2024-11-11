#Functions - are most logical and smaller block of codes that can be used repeatedly
#To execute the fucntion's code, you need to invoke/call teh function
def print_data():
    print("Hello world")
    print("How are you all?")
    print("It's a fine morning")
print_data()

def add_two_num():
    a = 5
    b = 10
    print(a + b)
add_two_num()

def sum_of_num(a,b): #Functions with parameters
    c = a + b
    print(c)
sum_of_num(5,10) # Arguments
sum_of_num(10,25)
sum_of_num(55,100)
sum_of_num(1000,1000000)

def add_more_num(a,b,c): #Functions with parameters
    d = a + b + c
    print(d)
add_more_num(10,20,30)

#Return keyword
def add_more_num(a, b, c): # Functions with parameters
    return a + b + c
sum_of_nums = add_more_num(100,10,1)
print(sum_of_nums)

#Interview question - *args & **kwargs
def sum_of_nums(*args): # * args is arbitrary num of arguments, it wil be in tuple format
    for num in args: #(10,20,30....)
        print(num)
    return sum(args)

l = sum_of_nums(1,2,3)
m = sum_of_nums(10,20,30,40,50,60)
n = sum_of_nums(0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8)
print(l, m, n)