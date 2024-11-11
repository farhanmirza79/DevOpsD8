#Interview question - *args & **kwargs
def sum_of_nums(*args): # * args is arbitrary num of arguments, it wil be in tuple format
    for num in args: #(10,20,30....)
        print(num)
    return sum(args)

l = sum_of_nums(1,2,3)
m = sum_of_nums(10,20,30,40,50,60)
n = sum_of_nums(0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8)
print(l, m, n)

def func(a, b, *args , c): # a, b, are positional parameters , *args arbitrary star parameters , c is named parameter
    print(a)
    print(b)
    print(*args)
    print(c)

func(1,2,4,5,6,7,8,9,10,100, c=100) # a, b are postional parameters, *args arbitary
def func(**kwargs): # {"a":1, "b":2 "c":3}
    for k, v in kwargs:
        print(k, v)
func(a=1, b=2, c=3) # Pass arguments as named arguments or key = value format

def func(a, b, *args , **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

func(1,2,3,4,5,6,7,8,9,10,11, X=100, y= 200, z = 300)

