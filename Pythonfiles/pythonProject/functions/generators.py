l = range(0,5)
print(l)

l = [1,2,3,4,5]
for num in l:
    print(num)


#Generators are the most easiest way of creating iterators in memory efficient way
#You can identify generator using yield key word
#Generators are used to create iteratros, but with a different approach.
#Generators are simple functions which returns an iterable set of items,one at a time.
#Identified by yield
def generate_numbers(n):
    for i in range(0, n):
        yield i # Its a generator that iterates every next element in given list or range
l = iter(generate_numbers(6))
print(next(l))
print(next(l))
print(next(l))

l = iter(generate_numbers(6))
for i in l:
    print(i)

l = [1,2,3,4,5,6]
sq_l = []
for num in l:
    sq_l.append(num ** 2)

def square_numbers(n):
    for i in range(1, n): # for i in range(1,10)
        yield i ** 2      # i ** 2

for num in square_numbers(10):
    print(num)

def read_large_file(file_path):
    with open(file_path, 'r') as f:
        for line in f:
            yield line

for l in read_large_file("path_of_file"):
    print(l)

#Generator expression
#Generator expression are similar to list comprehensions, but with parenthesis - ()

squares = (x ** 2 for x in range(0,10))
for num in squares:
    print(num)

#Generator chaining
#Generator chaining is a process of feeding the output of one generator to another generator
numbers = (i for i in range (1,10))

squares = (num ** 2 for num in numbers)

even_squares = (number for number in squares if number % 2 == 0)

for even_number in even_squares:
    print(even_number)


