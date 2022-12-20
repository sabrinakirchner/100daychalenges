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

bill = float(input("The value of the bill? \n"))
people = int(input("How many people in the table? \n"))
tip = float(input("How many tip would you like to give? 10%, 15%, 20% \n"))


tip2 = (tip*bill)/100
total_people = (tip2+bill)/people

print(f'The total of your bill with tip will be {bill+tip2} and the total divide per person will be {total_people}')


#________________________________________________________________________________________________#

