elapsed = 7835 # 1 minute = 60 miniutes - 1 hour = 60 mins 60 mins * 60 seconds
hours = 7835 // (60*60) # this will give the hour component
print(hours)
remaining_seconds = 7835 % (60 *60) #Remaining seconds after taking out hour component
minutes = remaining_seconds // 60 # minutes component from remaining seconds
print(minutes)
seconds = remaining_seconds % 60 # Remaining seconds after taking out minutes component
print(seconds)


a = None # none value - basically no value - just a placeholder in memory
if a == None:
    a = "N/A"
else:
    a = a
print(a)
#Ternary operator
a = "N/A" if a == None else a

print("*********************************************************")

credit_score = int(input("Enter your credit score"))
if credit_score > 0 and credit_score <580:
    rating = "Poor"
elif credit_score >= 580 and credit_score < 670:
    rating = "fair"
elif credit_score >=670 and credit_score < 740:
    rating = "Good"
elif credit_score >=740 and credit_score < 800:
    rating = "Very Good"
elif credit_score >=800 and credit_score <= 850:
    rating = "Excellent"
print(rating)

print("*********************************************************")

a = int(input("Enter a number: "))
if a % 2 == 0:
    print(f"The number {a} is even")
else:
    print(f"The number {a} is not even")

print("*********************************************************")
# Question 1
list_of_numbers = ["10","20","30","40","50","60","70","80","90","100"]
print(list_of_numbers[:5])
print(list_of_numbers[5:])
print(list_of_numbers[::2])
print(list_of_numbers[1::3])
print(list_of_numbers[::-1])

print("*********************************************************")
# Question 2
a = 1
if a <=1:
    print("The number is not prime")
if a == 6:
    print("The number is prime")


print("*********************************************************")

# Question 3

first_name = "Farhan"
last_name = "Mirza"
age = 29

greeting_message = f"Hello, {first_name} {last_name}! You are {age} years old."

print(greeting_message)



