# 09-11-24
age = 18
if age > 18:
    print("You are eligible to vote")
else:
    print("Your not eligible for voting")

if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible for voting")

print("*******************************************************************************************")

age = 25

if age < 13:
    print("You are a child")
elif (age > 13) and (age < 18):
    print("You are a teenager")
elif (age >18)  and (age < 65):
    print("You are an adult")
else:
    print("You are a senior citizen")

print("*******************************************************************************************")

marks = 63
if marks >= 95:
    grade = "A"
elif 85 < marks < 95:
    grade = "B"
elif 75 < marks < 85:
    grade = "C"
elif 65 < marks < 75:
    grade = "D"
elif 55 < marks <= 65:
    grade = "E"
else:
    grade ="F"
print(grade)

print("*******************************************************************************************")

account_active = True
account_balance = 10_000
withdrawal_amount = 5_000

if account_active and withdrawal_amount <= account_balance:
    remaining_balance = account_balance - withdrawal_amount
    print(remaining_balance)
    print("withdrawal completed")
else:
    print("withdrawal declined")
print("*******************************************************************************************")



