# Day 2 - 100 Days of Python Course

# Write your Day 2 code below:
print("Day 2 - Let's code!")

print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? "))

per = int(input("What percentage tip would you like to give? 10 , 12 , or 15? "))

people = int(input("How many people to split the bill? "))

bill_per = total_bill * (per / 100)
actual_result = total_bill + bill_per

res = actual_result / people

print("Each person should pay:", res)


# Task 2
# Calculate BodyMassIndex from user weight and height

weight = int(input("Enter your weight: "))
height = float(input("Enter your height: "))

BMI = weight / (height) ** 2
print(BMI)


# Task 3
# Add 2 digit nmber
print(39 / 10)
print("hey", 39 // 10)
print("bye", 39 % 10)

num = input("Enter num: ")
if len(num) < 3:
    num = int(num)
    d = 0
    c = num // 10
    d += c
    num = num % 10
    d += num
    print(d)
else:
    print("plz enter 2 digit nmbr")
