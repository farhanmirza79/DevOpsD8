age = 18
#Indentation
#Conditional statements
if age >=18:
    print("You are eligible for voting")
else:
    print("You are not eligible for voting")

age = 66
if age < 13:
    print("you are a child")
elif (age > 13) and (age < 18):# 13 <age < 18
    print ("you are a teenager")
elif (age > 18) and (age < 65):# 18 < age <65
    print ("you are an adult")
else:
    print("You are a senior citizen")

print("***************************")

marks = 45
if marks >= 95:
    grade = "A"
elif 85 < marks < 95:
    grade = "B"
elif 65 < marks < 85:
    grade = "C"
elif 55 < marks < 65:
    grade = "D"
else:
    grade = "F"
print(grade)

print("***************************")

account_active = True # Boolean value
account_balance = 10_000 #integer
withdrawal_amount = 5_000 #integer

if account_active and withdrawal_amount <= account_balance:
    remaining_balance = account_balance - withdrawal_amount
    print("withdrawal completed")
    print(remaining_balance)
else:
    print("withdrawal Declined")

print("***************************") # Nested

if age >=0:
    if age < 13:
        print("child")
        if age > 5 and age <8:
            print("naughty")
    elif age < 20:
        print("teenager")
    elif age < 65:
        print("Adult")
    else:
        print("senior citizen")
else:
    print("please enter a valid age")

petrol_price = 100
if petrol_price < 100:
    vol_petrol =2
else:
    vol_petrol =1

print(f"I want to pump {vol_petrol} liters of petrol") #Ternary operator

print("***************************")

vol_petrol =2 if petrol_price < 100 else 1
print(f"I want to pump {vol_petrol} liters of petrol")


print("***************************")  #Excerise
a = 5
if a:
    a = "N/A"
else:
    a = "None"
print(a)

print(f"")

#Given an credit  score, assign a string value to another variable rating based on the following scale:#





