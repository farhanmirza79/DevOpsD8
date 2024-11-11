# Interview questions - What is the difference between break, continue and pass
#BREAK

list_nums = [1,2,3,4,5,6,7]
for num in list_nums:
    if num % 2 == 0:
        print(f"{num} is even")
        if num == 6:
            
            break #abnormally terminate the loop/iteration

i = 0
while i <10:
    print(i)
    i = i + 1
    if i ==7:
        break # abnormaly terminate the loop

#CONTINUE

i = 0
while i < 10:
    print(i)
    i = i + 1
    if 1 == 7:
        continue # if continue condition is met, the remaining part of the code will not be executed for that iteration
    print(f"some code after continue")
    print(f"some more code after continue")
    a = 1
    b = 2
    c = a + b
    print(c)

#PASS

print("pass keyword execution example")
num = 3
if num % 2 == 0:
    pass # when there is no code to execute, empty block of code
else:
    print(f"num is odd")

i = 0
while i < 10:
    print(i)
    i = i + 1
    if i == 5:
        pass # empty block of code
    else:
        print("number has been incremented")