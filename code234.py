# 100 days coding
# course Udemy
# https://www.udemy.com/course/100-days-of-code/learn/lecture/17841382#questions




# switches the values

a = input("a: ")
b = input("b: ")
numb = a
a=b
b= numb
print("a: " + a)
print("b: " + b)

#______________________________________________#
#band name generator

print("Welcome to the Band Generator name!")

city = input("What is the city you grow up in?\n ")
pet = input("What is your pets name?\n ")

print(f'Your band name is {city} { pet}.')

#_______________________________________________________________#
#data type
two_digit_number = input("Type a two digit number: \n")

first_digits = two_digit_number[0]
second_digit = two_digit_number[1]

total = int(first_digits) + int(second_digit)

print(total)


#_____________________________________________________________________#

name = len(input("What is your name? \n"))
print(f'Your name has {name} characthers')

#_______________________________________________________________________#
#BMI
height = float(input("enter your height in m: \n"))
weight = float(input("enter your weight in kg: \n"))

bmi = float(weight / height / height)

print(round(bmi))

#_______________________

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

height2 = float(height)
weight2 = float(weight)

bmi = float(weight2 / height2 / height2)

print(round(bmi))


#_______________________________________________________________________#
#Life in Weeks

age = int(input("What is your current age? \n"))
old = 90

month = 12
week = 52
days = 365

result = (old - age)

total_month = result * month
total_week = result * week
total_days = result * days


print(f'You have {total_days} days, {total_week} weeks, and {total_month} months left.')


#______________________________________________________________________________________________#
#Tip calculator

print("Elcome to the tip calculator! \n")

bill = float(input("The value of the bill? \n"))

people = int(input("How many people in the table? \n"))

tip = float(input("How many tip would you like to give? 10%, 15%, 20% \n"))


tip2 = (tip*bill)/100
total_people = (tip2+bill)/people

print(f'The total of your bill with tip will be {bill+tip2} and the total divide per person will be {total_people}')

#_______________________________________________________________________________#
#simpler tip calculator as the exemple
print("Elcome to the tip calculator! \n")

bill = float(input("The value of the bill? \n"))

tip = float(input("How many tip would you like to give? 10%, 12%, 15% \n"))


tip2 = (tip*bill)/100
total_people = (tip2+bill)

print(f'The total of your bill with tip will be {round(bill+tip2,2)}')

#________________________________________________________________________________________________#
#  given number is an odd or even number.

number = int(input("Which number do you want to check? \n "))

even = number / 2
odd = number % 2

if odd :
    print(f'This is an odd number.')
elif even:
    print(f'This is an even number.')

#___________________________________________________________________________________________#
#new BMI



weight = int(input(" what is your weight: \n"))
height = float(input(" Whatis your height: \n"))
bmi = float (weight / height / height)


underweight = bmi < 18.5
normal = 18.5 <= bmi < 25
overweight = 25 <= bmi < 29.9
obesity = bmi >= 30

print("\n Your Bmi is ", bmi)

if underweight == True:
    print("\nYou are at the category Underweight ")
elif normal == True:
    print("\nYou are at the Normal category this is from 18.5 to 24.9")
elif overweight == True:
    print("\nYou are on the Overweight category this is from 25 to 29.9")
elif obesity == True:
    print("\nYou are on the Obesity category this is when your bmi is over 30")


#______________________________________________________________________________#
#BMI as the exemple

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = round((weight / height / height))

underweight = bmi < 18.5
normal = 18.5 <= bmi < 25
overweight = 25 <= bmi < 29.9
obesity = bmi >= 30
clinically = bmi > 40

if underweight == True:
    print(f'Your BMI is {bmi}, you are underweight')
elif normal == True:
    print(f'Your BMI is {bmi},  you have a normal weight')
elif overweight == True:
    print(f'Your BMI is {bmi},you are slightly overweight.')
elif obesity == True:
    print(f'Your BMI is {bmi}, you are obese.')
elif clinically == True:
    print(f'Your BMI is {bmi},  you are clinically obese.')

#_________________________________________________________________________________#
#Year leap
#google

year = int(input('Enter year:\n '))
if (year%4 == 0 and year%100 != 0) or (year%400 == 0):
    print(year, "leap year.")
else:
    print(year, "not a leap year.")

#___________________________________________________________________________________#
#Year leap
#mine

year = int(input("Which year do you want to check? \n "))

if (year%100 != 0) and (year%400 == 0):
    print("leap year")
elif year%4 == 0:
    print("leap year")
else:
    print("Not leap year.")

# ________________________________________________________________________________________#
# Pizza

print("Welcome to Python Pizza Deliveries! \n")

bill = 0

size = input("What size pizza do you want? S, M, or L \n ")

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25

add_pepperoni = input("Do you want pepperoni? Y or N \n")
if add_pepperoni == "Y":
    if size == "S":
        bill +=2
    else:
        bill +=3
else:
    print("no peperoni")

extra_cheese = input("Do you want extra cheese? Y or N \n")
if extra_cheese == "Y":
    bill += 1
else:
    print("No cheese!")

print(f'your total is {bill}. ')

# _______________________________________________________________________________#
# pizza as asked!

print("Welcome to Python Pizza Deliveries! \n")

size = input("What size pizza do you want? S, M, or L \n ")
add_pepperoni = input("Do you want pepperoni? Y or N \n")
extra_cheese = input("Do you want extra cheese? Y or N \n")

bill = 0

if size == "S":
    bill += 15
    if add_pepperoni == "Y":
        if size == "S":
            bill += 2
    if extra_cheese == "Y":
        bill += 1

elif size == "M":
    bill += 20
    if add_pepperoni == "Y":
        bill +=3
    if extra_cheese == "Y":
        bill += 1

elif size == "L":
    bill += 25
    if add_pepperoni == "Y":
        bill +=3
    if extra_cheese == "Y":
        bill += 1

print(f'Your Final bill is ${bill}.')

# ___________________________________________________________________________#
# Love Calculator
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
