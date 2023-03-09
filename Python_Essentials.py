print("The itsy bitsy spider climbed up the waterspout.")
print("Down came the rain and washed the spider out.")
#The program invokes the print() function twice.

print("The itsy bitsy spider climbed up the waterspout.")
print()
print("Down came the rain and washed the spider out.")

#/n moves code to the next line
print("The itsy bitsy spider\nclimbed up the waterspout.")
print()
print("Down came the rain\nand washed the spider out.")

#feeding the print() with more than one arguement
print("The itsy bitsy spider" , "climbed up" , "the waterspout.")

#Arguement end in use, with a space
print("My name is", "Python.", end=" ")
print("Monty Python.")

#Using the separator arguement "sep"
print("My", "name", "is", "Monty", "Python.", sep="-")

#Using both arguements "sep" and "end"
print("My", "name", "is", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*\n")

#Challenge lab: 
#Modify the first line of code in the editor, using the sep and end keywords, to match the expected output. Use the two print() functions in the editor.Don't change anything in the second print() invocation.

#Expected output
#(Programming***Essentials***in...Python)

print("Programming","Essentials","in", sep="***", end="...")
print("Python")


# Play with the code: 
# make the arrow twice as large (but keep the proportions)
#duplicate the arrow, placing both arrows side by side
#remove any of the quotes

print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")


print("with fewer 'print()' invocations:")
###################
print("    *\n   * *\n  *   *\n *     *\n***   ***")
print("  *   *\n  *   *\n  *****")
###################
print("higher:")
###################
print("        *")
print("       * *")
print("      *   *")
print("     *     *")
print("    *       *")
print("   *         *")
print("  *           *")
print(" *             *")
print("******     ******")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *******")
###################
print("doubled:")
###################
print("        *        "*2)
print("       * *       "*2)
print("      *   *      "*2)
print("     *     *     "*2)
print("    *       *    "*2)
print("   *         *   "*2)
print("  *           *  "*2)
print(" *             * "*2)
print("******     ******"*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *******     "*2)

#Strings:
# Use the escape character (\) to eencode the double quotes
print("I like \"Monty Python\"")

#Use apostrophe and quote interchangeably to delimit strings , but they must be used consistently
print('I like "Monty Python"')
print("I like 'Monty Python'")

#Lab Scenario: Write a one-line piece of code, using the print() function, 
# as well as the newline and escape characters, to match the expected result outputted on three lines.
# Expected output

# "I'm"
# ""learning""
# """Python"""

#Solution using single quotes
print('"I\'m"\n''""learning""\n''"""Python"""\n')

# Basic Operators
# They are 


# Exponentiation
# 
print(2 ** 3)
print(2 ** 3.)
print(2. ** 3)
print(2. ** 3.)

print(2 * 3)
print(2 * 3.)
print(2. * 3)
print(2. * 3.)

# Single slash (/)
print(6 / 3)
print(6 / 3.)
print(6. / 3)
print(6. / 3.)

# Double slash (//)
print(6 // 3)
print(6 // 3.)
print(6. // 3)
print(6. // 3.)

# Modulo
print(14 % 4)

# If the exponentiation operator uses right-sided binding
print(-3 ** 2)
print(-2 ** 3)
print(-(3 ** 2))

#Summary Questions
#Question 1: What is the expected output of the following snippet?

print((2 ** 4), (2 * 4.), (2 * 4))

#Question 2: What is the expected output of the following snippet?

print((-2 / 4), (2 / 4), (2 // 4), (-2 // 4))

#Question 3: What is the expected output of the following snippet?

print((2 % -4), (2 % 4), (2 ** 3 ** 2))

#Variables
#Initialising one is as below
var = 1
print(var)

#Print out name of a/c holder using var
var = 1
account_balance = 1000.0
client_name = 'John Doe'
print(var, account_balance, client_name)
print(var)

#Use print() function to combine text and var
var = "3.8.5"
print("Python version: " + var)

#The equal sign is an assignment operator
var = 1
print(var)
var = var + 1
print(var)

#Using var and its assignment power
var = 100
var = 200 + 300
print(var)

#Solving mathematical probles
#Construct a short program solving simple mathematical problems such as the Pythagorean theorem:

a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5
print("c =", c)

#LAB: Variable
# Scenario
#Here is a short story:

# Once upon a time in Appleland, John had three apples, Mary had five apples, and Adam had six apples. 
# They were all very happy and lived for a long time. End of story.

#Your task is to:

#1. create the variables: john, mary, and adam;
#2. assign values to the variables. The values must be equal to the numbers of fruit possessed by John, Mary, and Adam respectively;
#3. having stored the numbers in the variables, print the variables on one line, 
#   and separate each of them with a comma;
#4. now create a new variable named total_apples equal to the addition of the three previous variables.
#5. print the value stored in total_apples to the console;
#6. experiment with your code: create new variables, assign different values to them, and perform various arithmetic operations on them (e.g., +, -, *, /, //, etc.). Try to print a string and an integer together on one line, e.g., "Total number of apples:" and total_apples.

#Solution:
john_apples = 3
mary_apples = 5
adam_apples = 6
total_apples = (john_apples + mary_apples + adam_apples)
print(john_apples,mary_apples,adam_apples, sep=',')
print(total_apples)
print('Total number of apples:', total_apples)

# Shortcut Operators
x = x * 2
sheep = sheep + 1

# Python offers you a shortened way of writing operations like these:
x *= 2
sheep += 1

#  LAB   Variables ‒ a simple converter

# Miles and kilometers are units of length or distance.
# Bearing in mind that 1 mile is equal to approximately 1.61 kilometers, complete the program in the editor so that it converts:

#miles to kilometers;
#kilometers to miles.
#Do not change anything in the existing code. Write your code in the places indicated by ###. Test your program with the data we've provided in the source code.

#Pay particular attention to what is going on inside the print() function. 
# Analyze how we provide multiple arguments to the function, and how we output the expected data.

#Note that some of the arguments inside the print() function are strings (e.g., "miles is", whereas some other are variables (e.g., miles).

# Expected output
# 7.38 miles is 11.88 kilometers
# 12.25 kilometers is 7.61 miles

# Solution:
kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.61  
kilometers_to_miles = kilometers / 1.61

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")

#  LAB   Operators and expressions

# Scenario
#Take a look at the code in the editor: it reads a float value, puts it into a variable named x, and prints the value of a variable named y. 
# Your task is to complete the code in order to evaluate the following expression:

#    3x3 - 2x2 + 3x - 1

# Note how we change data type to make sure that x is of type float.
# The result should be assigned to y

#  x =  # Hardcode your test data here.
#  x = float(x)
#   Write your code here.
#  print("y =", y)

# Solution:
x = 0
x = float(x)
y = 3 * x**3 - 2 * x**2 + 3 * x - 1
print("y =", y)

x = 1
x = float(x)
y = 3 * x**3 - 2 * x**2 + 3 * x - 1
print("y =", y)

x = -1
x = float(x)
y = 3 * x**3 - 2 * x**2 + 3 * x - 1
print("y =", y)


# LAB   Comments
# Scenario
# The code in the editor contains comments. Try to improve it: 
# add or remove comments where you find it appropriate (yes, sometimes removing a comment can make the code more readable), 
# and change variable names where you think this will improve code comprehension.

# this program computes the number of seconds in a given number of hours
# this program has been written two days ago

a = 2 # number of hours
seconds = 3600 # number of seconds in 1 hour

print("Hours: ", a) #printing the number of hours
# print("Seconds in Hours: ", a * seconds) # printing the number of seconds in a given number of hours

#here we should also print "Goodbye", but a programmer didn't have time to write any code
#this is the end of the program that computes the number of seconds in 3 hour

# Solution:
#this program computes the number of seconds in a given number of hours
# this program has been written two days ago

a = 2 # number of hours
b = 3 # number of hours
seconds = 3600 # number of seconds in 1 hour

print("Hours: ", a) #printing the number of hours
print("Seconds in Hours: ", a * seconds) # printing the number of seconds in a given number of hours

print('Goodbye')#here we should also print "Goodbye", but a programmer didn't have time to write any code
print('Seconds in 3 Hours: ', b * seconds) #this is the end of the program that computes the number of seconds in 3 hour

# Input() variable
print("Tell me anything...")
anything = input()
print("Hmm...", anything, "... Really?")

# The input() function with an argument
anything = input("Tell me anything...")
print("Hmm...", anything, "...Really?")
 
# The result of input() function
anything = input("Enter a number: ")
something = anything ** 2.0
print(anything, "to the power of 2 is", something)

# Input() and type casting

leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
hypo = (leg_a**2 + leg_b**2) ** .5
print("Hypotenuse length is", hypo)

#removing the "hypo" variable makes the code clean
leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
print("Hypotenuse length is", (leg_a**2 + leg_b**2) ** .5)


# String operators
# The program glues strings together

fnam = input("May I have your first name, please? ")
lnam = input("May I have your last name, please? ")
print("Thank you.")
print("\nYour name is " + fnam + " " + lnam + ".")


# This simple program "draws" a rectangle, making use of an old operator (+)
print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")

# Replication
# replicates the string the same number of times specified by the number; this case generates a square box

print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")

# More examples:
# Example 2:
x, y, z = 5, 10, 8
 
print(x > z)
print((y - 5) == x)

# Example 2:
x, y, z = 5, 10, 8
x, y, z = z, y, x
 
print(x > z)
print((y - 5) == x)

#  LAB   Simple input and output
# Scenario
# Your task is to complete the code in order to evaluate the results of four basic arithmetic operations.

# The results have to be printed to the console.

# You may not be able to protect the code from a user who wants to divide by zero. 
# That's okay, don't worry about it for now.

# input a float value for variable a here
# input a float value for variable b here

# output the result of addition here
# output the result of subtraction here
# output the result of multiplication here
# output the result of division here

# print("\nThat's all, folks!")

# Solution:

a = float(input("Give (a) a value: "))
# input a float value for variable b here
b = float(input("Give (b) a value: "))
# output the result of addition here
print("Addition result:", a + b)
# output the result of subtraction here
print("Subtraction result:", a - b)
# output the result of multiplication here
print("Multiplication result:", a * b)
# output the result of division here
print("Division result:", a / b)

print("\nThat's all, folks!")

#  LAB   Operators and expressions
# Scenario
# Your task is to complete the code in order to evaluate the following expression

# Sample input:1    Expected output: y = 0.6000000000000001

# Solution:

x = float(input("Enter value for x: "))


# Write your code here.
y = 1 / (x + 1 /(x + 1 / (x + (1 / x))))
print("y =", y)

#  LAB   Operators and expressions – 2
# Scenario
# Your task is to prepare a simple code able to evaluate the end time of a period of time, given as a number of minutes (it could be arbitrarily large). 
# The start time is given as a pair of hours (0..23) and minutes (0..59). The result has to be printed to the console.

# For example, if an event starts at 12:17 and lasts 59 minutes, it will end at 13:16.

# Don't worry about any imperfections in your code ‒ it's okay if it accepts an invalid time ‒ the most important thing is that the code produces valid results for valid input data.
# Sample input: 12 , 17, 59     Expected output:13:16

# Solution:
hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))
mins = mins + dura # find a total of all minutes
hour = hour + mins // 60 # find a number of hours hidden in minutes and update the hour
mins = mins % 60 # correct minutes to fall in the (0..59) range
hour = hour % 24 # correct hours to fall in the (0..23) range
print(hour, ":", mins, sep='')

# Equality operator (==)
var = 0  # Assigning 0 to var
print(var == 0)
var = 1  # Assigning 1 to var
print(var == 0)

# Code Examples:
# Example 1:
x = 10
 
if x == 10:
    print(x == 10)
if x > 5:
    print(x > 5)
if x < 10:
    print(x < 10)
else:
    print("else")
 

# Inequality: the not equal to operator (!=)
var = 0  # Assigning 0 to var
print(var != 0)
var = 1  # Assigning 1 to var
print(var != 0)

# Comparison operators: greater than (>)
black_sheep > white_sheep  # Greater than

# Comparison operators: greater than or equal to (>=)
centigrade_outside >= 0.0  # Greater than or equal to

# Comparison operators: less than (<)
centigrade_outside < 0.0  # Less than

# Comparison operators: less than or equal to (<=)
centigrade_outside <= 0.0  # Less than or equal to

#  LAB:   Variables
# Scenario
# Using one of the comparison operators in Python, write a simple two-line program that takes the parameter n as input, which is an integer, and prints False if n is less than 100, and True if n is greater than or equal to 100.
# Don't create any if blocks (we're going to talk about them very soon). Test your code using the data we've provided for you.

# Test Data
# Sample input: 55  Expected output: False
n = int(input('Give me a number:'))
print( n >= 100)

# Conditions and conditional execution
# the if statement

sheep_counter = 120
if sheep_counter >= 120: # Evaluate a test expression
    sleep_and_dream() # Execute if test expression is True

# the if-else statement

if true_or_false_condition:
    perform_if_condition_true
else:
    perform_if_condition_false

# Nested if statement

if the_weather_is_good:
    if nice_restaurant_is_found:
        have_lunch()
    else:
        eat_a_sandwich()
else:
    if tickets_are_available:
        go_to_the_theater()
    else:
        go_shopping()

# Example code: Find the larger number

# Read two numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

# Choose the larger number
if number1 > number2:
    larger_number = number1
else:
    larger_number = number2

# Print the result
print("The larger number is:", larger_number)


# Write a program which finds the largest of four, five, six, or even ten numbers
first_number = int(input('Select a number between 1 to 6 and pick one:'))
second_number = int(input('Select a number between 1 to 6 and pick a different one:'))
third_number = int(input('Select a number between 1 to 6 and pick another different one:'))

print('The numbers picked are:' , first_number , second_number , third_number , sep=',')
if first_number > second_number:
    print (first_number ,  "is greater than" , second_number)
else:
    print(second_number ,"is greater than" , first_number)
if first_number > third_number:
    print (first_number ,"is greater than" , third_number)
else:
    print(third_number ,"is greater than" , first_number)
if second_number > third_number:
    print (second_number ,"is greater than" , third_number)
else:
    print(third_number ,"is greater than" , second_number)

# Python inbuilt function MAX()
# Read three numbers.
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

# Check which one of the numbers is the greatest
# and pass it to the largest_number variable.

largest_number = max(number1, number2, number3)

# Print the result.
print("The largest number is:", largest_number)

# LAB   Comparison operators and conditional execution
# Scenario
# Spathiphyllum, more commonly known as a peace lily or white sail plant, is one of the most popular indoor houseplants that filters out harmful toxins from the air. Some of the toxins that it neutralizes include benzene, formaldehyde, and ammonia.
# Imagine that your computer program loves these plants. Whenever it receives an input in the form of the word Spathiphyllum, it involuntarily shouts to the console the following string: "Spathiphyllum is the best plant ever!"

# Write a program that utilizes the concept of conditional execution, takes a string as input, and:

# prints the sentence "Yes - Spathiphyllum is the best 
# plant ever!" to the screen if the inputted string is "Spathiphyllum" (upper-case)
# prints "No, I want a big Spathiphyllum!" if the inputted string is "spathiphyllum" (lower-case)
# prints "Spathiphyllum! Not [input]!" otherwise. Note: [input] is the string taken as input.
# Test your code using the data we've provided for you. And get yourself a Spathiphyllum, too!


# Test Data: Sample input: spathiphyllum  Expected output: No, I want a big Spathiphyllum!

# SOLUTION
word = input("What flower name do you have in mind?")

if word == 'spathiphyllum':
    print("No, I want a big Spathiphyllum!")
else:
    if word == 'pelargonium':
        print("Spathiphyllum! Not" , word , end="!")
    else:
        print('Yes - Spathiphyllum is the best plant ever!')
    

# Code Examples:
# Example 1:
x = "1"
 
if x == 1:
    print("one")
elif x == "1":
    if int(x) > 1:
        print("two")
    elif int(x) < 1:
        print("three")
    else:
        print("four")
if int(x) == 1:
    print("five")
else:
    print("six")

# Example 2:
x = 1
y = 1.0
z = "1"
 
if x == y:
    print("one")
if y == int(z):
    print("two")
elif x == y:
    print("three")
else:
    print("four")

# An infinite loop
# Store the current largest number here.
largest_number = -999999999

# Input the first value.
number = int(input("Enter a number or type -1 to stop: "))

# If the number is not equal to -1, continue.
while number != -1:
# Is number larger than largest_number?
    if number > largest_number:
# Yes, update largest_number.
        largest_number = number
# Input the next number.
        number = int(input("Enter a number or type -1 to stop: "))

# Print the largest number.
print("The largest number is:", largest_number)

# LAB   Essentials of the if-else statement
# Scenario
# Once upon a time there was a land – a land of milk and honey, inhabited by happy and prosperous people. The people paid taxes, of course – their happiness had limits. The most important tax, called the Personal Income Tax (PIT for short) had to be paid once a year, and was evaluated using the following rule:

# if the citizen's income was not higher than 85,528 thalers, the tax was equal to 18% of the income minus 556 thalers and 2 cents (this was what they called tax relief)
# if the income was higher than this amount, the tax was equal to 14,839 thalers and 2 cents, plus 32% of the surplus over 85,528 thalers.
# Your task is to write a tax calculator.

# It should accept one floating-point value: the income.
# Next, it should print the calculated tax, rounded to full thalers. There's a function named round() which will do the rounding for you – you'll find it in the skeleton code in the editor.
# Note: this happy country never returned any money to its citizens. If the calculated tax was less than zero, it would only mean no tax at all (the tax was equal to zero). Take this into consideration during your calculations.

# Look at the code in the editor – it only reads one input value and outputs a result, so you need to complete it with some smart calculations.

# Test your code using the data we've provided.


# Test Data: Sample input: 10000  Expected output:The tax is: 1244.0 thalers
#            Sample input: 100000 Expected output:The tax is: 19470.0 thalers
#            Sample input: 1000   Expected output:The tax is: 0.0 thalers
#            Sample input: -100   Expected output:The tax is: 0.0 thalers


# SOLUTION:
income = float(input("What's the annual income? : "))

if income < 85528:
	taxes = income * 0.18 - 556.02
else:
	taxes = (income - 85528) * 0.32 + 14839.02

if taxes < 0.0:
	taxes = 0.0

taxes = round(taxes, 0)
print("Tax to be paid is:", taxes, "thalers")
 
# LAB   Essentials of the if-elif-else statement
# Scenario
# As you surely know, due to some astronomical reasons, years may be leap or common. The former are 366 days long, while the latter are 365 days long.

# Since the introduction of the Gregorian calendar (in 1582), the following rule is used to determine the kind of year:

# if the year number isn't divisible by four, it's a common year;
#  otherwise, if the year number isn't divisible by 100, it's a leap year;
#  otherwise, if the year number isn't divisible by 400, it's a common year;
#  otherwise, it's a leap year.
# Look at the code in the editor – it only reads a year number, and needs to be completed with the instructions implementing the test we've just described.

# The code should output one of two possible messages, which are Leap year or Common year, depending on the value entered.

# It would be good to verify if the entered year falls into the Gregorian era, and output a warning otherwise: Not within the Gregorian calendar period. Tip: use the != and % operators.

# Test your code using the data we've provided.


# Test Data: Sample input: 2000   Expected output: Leap year
#            Sample input: 2015   Expected output: Common year
#            Sample input: 1999   Expected output: Common year  
#            Sample input: 1996   Expected output: Leap year
#            Sample input: 1580   Expected output: Not within the Gregorian calendar period

# SOLUTION:
year = int(input("Enter a year: "))

if year < 1582:
	print("Not within the Gregorian calendar period")
else:
    #  Write the if-elif-elif-else block here.
    if year % 4 != 0:
        print("Its a common year") # if the year number isn't divisible by four, it's a common year;
    elif year % 100 != 0:
        print("Its a leap year") # if the year number isn't divisible by 100, it's a leap year;
    elif year % 400 !=0: 
        print("Its a common year") # otherwise, if the year number isn't divisible by 400, it's a common year;
    else:
        print("It's a leap year!") # it's a leap year.

# The WHILE loop

# A program that reads a sequence of numbers
# and counts how many numbers are even and how many are odd.
# The program terminates when zero is entered.

odd_numbers = 0
even_numbers = 0

# Read the first number.
number = int(input("Enter a number or type 0 to stop: "))

# 0 terminates execution.
while number != 0:
# Check if the number is odd.
    if number % 2 == 1:
# Increase the odd_numbers counter.
        odd_numbers += 1
    else:
# Increase the even_numbers counter.
        even_numbers += 1
# Read the next number.
number = int(input("Enter a number or type 0 to stop: "))

# Print results.
print("Odd numbers count:", odd_numbers)
print("Even numbers count:", even_numbers)


# While loop Game: Guess the secret number
secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

guessed_number = int(input("Guess the secret number: "))

while guessed_number != secret_number:
    print("Ha ha! You're stuck in my loop!")
    guessed_number = int(input("Enter the number again: "))
print(secret_number, "Well done, muggle! You are free now.")

# For Loops
# Using the range() function
for i in range(10): 
    print("The value of i is currently", i) # Prints consequent numbers starting from zero

# Using 2 arguements in the range() function
for i in range(2, 8): 
    # The first argument determines the initial (first) value of the control variable.
    # The last argument shows the first value the control variable will not be assigned.
    print("The value of i is currently", i)

# Using 3 arguements in the range() function
for i in range(2, 8, 3):
    print("The value of i is currently", i)

# Explanation: 2 (starting number) → 5 (2 increment by 3 equals 5 – the number is within the range from 2 to 8)
#  → 8 (5 increment by 3 equals 8 – the number is not within the range from 2 to 8, 
# because the stop parameter is not included in the sequence of numbers generated by the function.)


# Particular Range() Situations that result to No Outputs 
# 1. Where range() function is empty
for i in range(1, 1):
    print("The value of i is currently", i)



# 2.  Where the set generated by the range() has to be sorted in ascending order
#   There's no way to force the range() to create a set in a different form when the range() function accepts exactly two arguments. 
#   This means that the range()'s second argument must be GREATER than the first
for i in range(2, 1):
    print("The value of i is currently", i)

# Program whose task is to write some of the first powers of two
starting_number = 1
for exponent in range(16):
    print("2 raised to the power of", exponent, "is", starting_number)
    starting_number *= 2

# break and continue statements

# break - example
print("The break instruction:")
for i in range(1, 6):
    if i == 3:
        break
    print("Inside the loop.", i)
print("Outside the loop.")

# continue - example
print("\nThe continue instruction:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Inside the loop.", i)
print("Outside the loop.")

# More Examples 
# break variant
largest_number = -99999999
counter = 0

while True:
    number = int(input("Enter a number or type -1 to end the program: "))
    if number == -1:
        break
    counter += 1
    if number > largest_number:
        largest_number = number

if counter != 0:
    print("The largest number is", largest_number)
else:
    print("You haven't entered any number.")

# continue variant
largest_number = -99999999
counter = 0

number = int(input("Enter a number or type -1 to end program: "))

while number != -1:
    if number == -1:
        continue
    counter += 1

    if number > largest_number:
        largest_number = number
    number = int(input("Enter a number or type -1 to end the program: "))

if counter:
    print("The largest number is", largest_number)
else:
    print("You haven't entered any number.")


# LAB
#  Your task is very simple here: write a program that uses a for loop to "count mississippily" to five. 
#  Having counted to five, the program should print to the screen the final message "Ready or not, here I come!"

# Solution:
import time

for second in range(1, 6):
    print(second, "Mississippi")
    time.sleep(1)
	
print("Ready or not, here I come!")

# LAB   The break statement – Stuck in a loop

#  The break statement is used to exit/terminate a loop.
#  Design a program that uses a while loop and continuously asks the user to enter a word unless the user enters "chupacabra" 
#  as the secret exit word, in which case the message "You've successfully left the loop." should be printed to the screen, and the loop should terminate.

# Don't print any of the words entered by the user. Use the concept of conditional execution and the break statement.

# Solution:
while True:
    word = input("You're stuck in an infinite loop!\nEnter the secret word to leave the loop: ")
    if word == "chupacabra":
        break
print("You've successfully left the loop!")


#  LAB   Essentials of the while loop

# Scenario
# Listen to this story: a boy and his father, a computer programmer, are playing with wooden blocks. They are building a pyramid.
# Their pyramid is a bit weird, as it is actually a pyramid-shaped wall – it's flat. 
# The pyramid is stacked according to one simple principle: each lower layer contains one block more than the layer above.

# Your task is to write a program which reads the number of blocks the builders have, 
# and outputs the height of the pyramid that can be built using these blocks.

# Test Data: Sample input: 6        Expected output:  The height of the pyramid: 3
#            Sample input: 20       Expected output:  The height of the pyramid: 3
#            Sample input: 1000     Expected output:  The height of the pyramid: 44
#            Sample input: 2        Expected output:  The height of the pyramid: 1

# SOLUTION
blocks = int(input("Enter the number of blocks: "))

height = 0
in_layer = 1
while in_layer <= blocks:
    height += 1
    blocks -= in_layer
    in_layer += 1

print("The height of the pyramid:", height)


#   LAB   Collatz's hypothesis
#   Scenario
# In 1937, a German mathematician named Lothar Collatz formulated an intriguing hypothesis (it still remains unproven) which can be described in the following way:take any non-negative and non-zero integer number and name it c0;
#       if it's even, evaluate a new c0 as c0 ÷ 2;
#       otherwise, if it's odd, evaluate a new c0 as 3 × c0 + 1;
#       if c0 ≠ 1, go back to point 2.
# The hypothesis says that regardless of the initial value of c0, it will always go to 1.
# Of course, it's an extremely complex task to use a computer in order to prove the hypothesis for any natural number (it may even require artificial intelligence), but you can use Python to check some individual numbers. Maybe you'll even find the one which would disprove the hypothesis.
# Write a program which reads one natural number and executes the above steps as long as c0 remains different from 1. We also want you to count the steps needed to achieve the goal. Your code should output all the intermediate values of c0, too.
#   Hint: the most important part of the problem is how to transform Collatz's idea into a while loop – this is the key to success.

# SOLUTION
c0 = int(input("Enter c0: "))

if c0 > 1:
	steps = 0
	while c0 != 1:
		if c0 %2 != 0:
			cnew = 3 * c0 + 1
		else:
			cnew = c0 // 2
		print(c0)
		c0 = cnew
		steps += 1
	print("steps =",steps)
else:
	print("Bad c0 value")
	
# Bit Mask
mask = 8
flag_register = 0000000000000000000000000000x000

if flag_register & mask:
    # My bit is set.
    print("My bit is set")
else:
    print("The Bit Mask Function applied: ")
    # My bit is reset.


# Shifting (Right and Left)
var = 17
var_right = var >> 1
var_left = var << 2
print(var, var_left, var_right)

# more quizez
# Prints output as False
x = 1
y = 0

z = ((x == y) and (x == y)) or not(x == y)
print(not(z))

# more quizez
# Prints out 0 5 -5 1 1 16
x = 4
y = 1

a = x & y
b = x | y
c = ~x # tricky!
d = x ^ 5
e = x >> 2
f = x << 2

print(a, b, c, d, e, f)

# Sorting

# Making the value of the fifth element to be copied to the second element 
numbers = [10, 5, 7, 2, 1]
print("Original list contents:", numbers) # Printing original list contents.

numbers[0] = 111
print("\nPrevious list contents:", numbers) # Printing previous list contents.

numbers[1] = numbers[4] # Copying value of the fifth element to the second.
print("New list contents:", numbers) # Printing current list contents.


# More: 
numbers = [10, 5, 7, 2, 1]
print("Original list contents:", numbers)  # Printing original list contents.

numbers[0] = 111
print("\nPrevious list contents:", numbers)  # Printing previous list contents.

numbers[1] = numbers[4]  # Copying value of the fifth element to the second.
print("Previous list contents:", numbers)  # Printing previous list contents.

# This is the len() function
print("\nList length:", len(numbers))  # Printing the list's length.


# Delete instruction

numbers = [10, 5, 7, 2, 1]
print("Original list content:", numbers)  # Printing original list content.
numbers[0] = 111
print("\nPrevious list content:", numbers)  # Printing previous list content.
numbers[1] = numbers[4]  # Copying value of the fifth element to the second.
print("Previous list content:", numbers)  # Printing previous list content.
print("\nList's length:", len(numbers))  # Printing previous list length.

###

del numbers[1]  # Removing the second element from the list.
print("New list's length:", len(numbers))  # Printing new list length.
print("\nNew list content:", numbers)  # Printing current list content.

###

# Negative Indices
# It prints the last item on the list

numbers = [111, 7, 2, 1]
print(numbers[-1])


# LAB   The basics of lists
#  Scenario
#  There once was a hat. The hat contained no rabbit, but a list of five numbers: 1, 2, 3, 4, and 5.

#  Your task is to:

#  write a line of code that prompts the user to replace the middle number in the list with an integer number entered by the user (Step 1)
#  write a line of code that removes the last element from the list (Step 2)
#  write a line of code that prints the length of the existing list (Step 3).


# SOLUTION:
hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.

# Step 1: write a line of code that prompts the user
# to replace the middle number with an integer number entered by the user.
hat_list[2] = int(input('Enter a number of your choice:'))
# Step 2: write a line of code that removes the last element from the list.
del hat_list[4]
# Step 3: write a line of code that prints the length of the existing list.
print(len(hat_list))
print(hat_list)


# METHODS
# A typical method invocation usually looks like this:

#  result = data.method(arg)


# Adding elements to a list: append() and insert()
numbers = [111, 7, 2, 1]
print(len(numbers))
print(numbers)

###

numbers.append(4)

print(len(numbers))
print(numbers)

###

numbers.insert(0, 222)
print(len(numbers))
print(numbers)


# Example of creating an empty list with for loop
my_list = []  # Creating an empty list.

for i in range(5):
    my_list.append(i + 1)

print(my_list)

#  Prints the reverse
my_list = [] # Creating an empty list.

for i in range(5):
    my_list.insert(0, i + 1)

print(my_list)


# Making use of lists
# Effeciency of for loops
my_list = [10, 1, 8, 3, 5]
total = 0

for i in range(len(my_list)):
    total += my_list[i]

print(total)

# The above code changes to this:
my_list = [10, 1, 8, 3, 5]
total = 0

for i in my_list:
    total += i

print(total)

# Swapping items in a list
my_list = [10, 1, 8, 3, 5]

my_list[0], my_list[4] = my_list[4], my_list[0]
my_list[1], my_list[3] = my_list[3], my_list[1]

print(my_list)

# using for loop to swap items on a list
for i in range(length // 2):
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i] #declare length variable as: length = len(list_name)
print(my_list)

# LAB
#  Scenario:

#The Beatles were one of the most popular music groups of the 1960s, and the best-selling band in history. 
# Some people consider them to be the most influential act of the rock era. 
# Indeed, they were included in Time magazine's compilation of the 20th Century's 100 most influential people.

# The band underwent many line-up changes, culminating in 1962 with the line-up of John Lennon, 
# Paul McCartney, George Harrison, and Richard Starkey (better known as Ringo Starr).


#Write a program that reflects these changes and lets you practice with the concept of lists. Your task is to:

#step 1: create an empty list named beatles;
#step 2: use the append() method to add the following members of the band to the list: John Lennon, Paul McCartney, and George Harrison;
#step 3: use the for loop and the append() method to prompt the user to add the following members of the band to the list: 
#        Stu Sutcliffe, and Pete Best;
#step 4: use the del instruction to remove Stu Sutcliffe and Pete Best from the list;
#step 5: use the insert() method to add Ringo Starr to the beginning of the list.

# SOLUTION:
# step 1:
Beatles = []
print("Step 1:", Beatles)

# step 2:

Beatles.append("John Lennon")
Beatles.append("Paul McCartney")
Beatles.append("George Harrison")
print("Step 2:", Beatles)

# step 3:
for members in range(2):
    Beatles.append(input("New band member: "))
print("Step 3:", Beatles)

# step 4:
del Beatles[-1]
del Beatles[-1]
print("Step 4:", Beatles)

# step 5:
Beatles.insert(0, "RingoStarr")
print("Step 5:", Beatles)
print("The Fab:",len(Beatles))


# Sorting a list
my_list = [8, 10, 6, 2, 4] # list to sort

for i in range(len(my_list) - 1): # we need (5 - 1) comparisons
    if my_list[i] > my_list[i + 1]: # compare adjacent elements
        my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i] # If we end up here, we have to swap the elements.



# Bubble Sort:
my_list = []
swapped = True
num = int(input("How many elements do you want to sort: "))

for i in range(num):
    val = float(input("Enter a list element: "))
    my_list.append(val)

while swapped:
    swapped = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print("\nSorted:")
print(my_list)


# Using sorting after assigning 
a = 3
b = 1
c = 2
 
lst = [a, c, b]
lst.sort()
 
print(lst)

# Using reverse sorting after assigning 
a = "A"
b = "B"
c = "C"
d = " "

lst = [a, b, c, d]
lst.reverse()

print(lst)

# inner life of lists
list_1 = [1]
list_2 = list_1
list_1[0] = 2
print(list_2)

# SLICE: Allows you to make a brand new copy of a list, or parts of a list. 

# General forms of the slice look as follows:

my_list[start:end] # The colon is the differenciating factor

# Sample codebase
list_1 = [1]
list_2 = list_1[:]
list_1[0] = 2
print(list_2)

# Copying the entire list.
list_1 = [1]
list_2 = list_1[:]
list_1[0] = 2
print(list_2)

# Copying some part of the list.
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]
print(new_list)

# This is how negative indices work with the slice:

my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:-1]
print(new_list)

# If the start specifies an element lying further than the one described by the end (from the list's beginning), the slice will be empty:

my_list = [10, 8, 6, 4, 2]
new_list = my_list[-1:1]
print(new_list)

# If you omit the start in your slice, it is assumed that you want to get a slice beginning at the element with index 0.

# In other words, the slice of this form: my_list[:end]is a more compact equivalent of: my_list[0:end]

my_list = [10, 8, 6, 4, 2]
new_list = my_list[:3]
print(new_list)

# Deleting all the elements at once is possible too:

my_list = [10, 8, 6, 4, 2]
del my_list[:]
print(my_list)

# 
# Removing list slice
# The print() function invocation from the last line of the code will then cause a runtime error.
my_list1 = [10, 8, 6, 4, 2]
del my_list1
print(my_list1)

# The in and not in operators
# Python offers two very powerful operators, 
# able to look through the list in order to check whether a specific value is stored inside the list or not.

elem in my_list
elem not in my_list

# Sample code:
my_list = [0, 3, 12, 8, 2]

print(5 in my_list)
print(5 not in my_list)
print(12 in my_list)

# SAMPLE IDEAL REAL WORLD APPLICATION 

# Let's assume that you've chosen the following numbers in the lottery: 3, 7, 11, 42, 34, 49
# The numbers that have been drawn are: 5, 11, 9, 42, 3, 49.
# The question is: how many numbers have you hit?

# Program:
drawn = [5, 11, 9, 42, 3, 49]
bets = [3, 7, 11, 42, 34, 49]
hits = 0
 
for number in bets:
    if number in drawn:
        hits += 1
 
print(hits)

# LAB 
# Scenario

# Imagine a list ‒ not very long, not very complicated, just a simple list containing some integer numbers. 
# Some of these numbers may be repeated, and this is the clue. We don't want any repetitions. We want them to be removed.
# Your task is to write a program which removes all the number repetitions from the list. 
# The goal is to have a list in which all the numbers appear not more than once.

#   Note: assume that the source list is hard-coded inside the code ‒ you don't have to enter it from the keyboard. 
#   Of course, you can improve the code and add a part that can carry out a conversation with the user and obtain all the data from her/him.

# Hint: we encourage you to create a new list as a temporary work area ‒ you don't need to update the list in situ.

# We've provided no test data, as that would be too easy. You can use our skeleton instead.

# SOLUTION
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
new_list = []
for number in my_list:  # Browse all numbers from the source list.
	if number not in new_list:  # If the number doesn't appear within the new list...
		new_list.append(number)  # ...append it here.
my_list = new_list[:]  # Make a copy of new_list.
print("The list with unique elements only:")
print(my_list)


# list of lists representing the whole chessboard
# Two dimensional data array are reffered to as a MATRIX


# Three dimensional data array
rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]


# FUNCTIONS
# defining our prompting function ‒ here it is:

def message():
    print("Enter a value: ")

# 1. You mustn't invoke a function which is not known at the moment of invocation.
print("We start here.")
message()
print("We end here.")
 
 
def message():
    print("Enter a value: ")


# 2. You mustn't have a function and a variable of the same name.
# The following snippet is erroneous:

def message():
    print("Enter a value: ")
 
message = 1

# You're free to mix your code with functions ‒ you're not obliged to put all your functions at the top of your source file.

print("We start here.")
 
def message():
    print("Enter a value: ")
 
message()
 
print("We end here.")


# Function at work
# Modifying the prompting message is now easy and clear - you can do it by changing the code in just one place ‒ inside the function's body.

def message():
    print("Enter a value: ")
 
message()
a = int(input())
message()
b = int(input())
message()
c = int(input())
 
# Parameterized functions
#  
def choice(number):
    print("Enter a number of your choice:", number)

choice(4)

# It's legal, and possible, to have a variable named the same as a function's parameter.
# A situation like this activates a mechanism called shadowing:
# The snippet illustrates the phenomenon:

def message(number):
    print("Enter a number:", number)
 
number = 1234
message(1)
print(number)

# A function can have as many parameters as you want, 
#  but the more parameters you have, the harder it is to memorize their roles and purposes.

# Modifying the function ‒ it has two parameters now:
def message(what, number):
    print("Enter", what, "number", number)

message("telephone", 11)
message("price", 5)
message("number", "number")


# Positional parameter passing
# A technique which assigns the ith (first, second, and so on) argument to the ith (first, second, and so on) function parameter

def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)
 
introduction("Luke", "Skywalker")
introduction("Jesse", "Quick")
introduction("Clark", "Kent")


# Keyword argument passing
#  Here the meaning of the argument is dictated by its name, not by its position
def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)

introduction(first_name = "James", last_name = "Bond")
introduction(last_name = "Skywalker", first_name = "Luke")

# Mixing positional and keyword arguments
# You can mix both styles if you want ‒ there is only one unbreakable rule: you have to put positional arguments before keyword arguments.

def adding(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)

adding(1, 2, 3)

#  replace such an invocation with a purely keyword variant
def adding(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)
adding(c = 1, b = 2, a = 3)

# function invocation + explaination
# the argument (3) for the a parameter is passed using the positional way;
# the arguments for c and b are specified as keyword ones.

def adding(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)
adding(3, c = 1, b = 2)
# Output: 3 + 2 + 1 = 6

# Parametrized functions – more details
def introduction(first_name, last_name="Smith"):
     print("Hello, my name is", first_name, last_name)
introduction("James" , "Doe")


def introduce(first_name, last_name="Smith"):
    print("Hello, my name is", first_name, last_name)
introduce("Henry")

# Output: Hello, my name is Henry Smith
 

#                 or this

def introduce(first_name, last_name="Smith"):
    print("Hello, my name is", first_name, last_name)
introduce(first_name="William")

# Output: Hello, my name is William Smith

# Functions: Effects & Returns
# Use return to make a function return a value

def happy_new_year(wishes = True):
    print("Three...")
    print("Two...")
    print("One...")
    if not wishes:
        return
 
    print("Happy New Year!")

# return with an expression
def boring_function():
    return 123

x = boring_function()

print("The boring_function has returned its result. It's:", x)

# None: 
# Is a KEYWORD
# Its data doesn't represent any reasonable value ‒ actually, 
# it's not a value at all; hence, it mustn't take part in any expressions.

print(None + 2) # will output nontype error

# differnt instance
value = None
if value is None:
    print("Sorry, you don't carry any value")

#           or

def strange_function(n):
    if(n % 2 == 0):
        return True
print(strange_function(2))
print(strange_function(1))


# LAB   
#  A leap year: writing your own functions
# Your task is to write and test a function which takes one argument (a year) and returns True if the year is a leap year, or False otherwise.

# The seed of the function is already sown in the skeleton code in the editor.

# Note: we've also prepared a short testing code, which you can use to test your function.

# The code uses two lists ‒ one with the test data, and the other containing the expected results. 
# The code will tell you if any of your results are invalid.

def is_year_leap(year):
    #
    # Write your code here.
    #

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr,"->",end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")


# SOLUTION
def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr,"-> ",end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")



#  LAB  
#   How many days: writing and using your own functions
# Your task is to write and test a function which takes two arguments (a year and a month) and returns the number of days for the given year-month pair (while only February is sensitive to the year value, your function should be universal).

# The initial part of the function is ready. Now, convince the function to return None if its arguments don't make sense.

# Of course, you can (and should) use the previously written and tested function (LAB 4.3.1.6). It may be very helpful. We encourage you to use a list filled with the months' lengths. You can create it inside the function ‒ this trick will significantly shorten the code.

# We've prepared a testing code. Expand it to include more test cases.
def is_year_leap(year):
    #
    # Your code from the previous LAB.
    #

def days_in_month(year, month):
    #
    # Write your new code here.
    #

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")

# SOLUTION
def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def days_in_month(year,month):
    if year < 1582 or month < 1 or month > 12:
        return None
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    res  = days[month - 1]
    if month == 2 and is_year_leap(year):
        res = 29
    return res

test_years = [1900, 2000, 2016, 1987]
test_months = [ 2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr,mo,"-> ",end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")

# LAB   
#  Day of the year: writing and using your own functions
# Your task is to write and test a function which takes three arguments (a year, a month, and a day of the month) and returns the corresponding day of the year, or returns None if any of the arguments is invalid.

# Use the previously written and tested functions. Add your own test cases to the code.

def is_year_leap(year):
    #
    # Your code from the previous LAB.
    #
def days_in_month(year, month):
    #
    # Your code from the previous lab.
    #
def day_of_year(year, month, day):
    #
    # Write your new code here.
    #
print(day_of_year(2000, 12, 31))

# SOLUTION:
def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def days_in_month(year, month):
    if year < 1582 or month < 1 or month > 12:
        return None
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    res  = days[month - 1]
    if month == 2 and is_year_leap(year):
        res = 29
    return res

def day_of_year(year, month, day):
    days = 0
    for m in range(1, month):
        md = days_in_month(year, m)
        if md == None:
            return None
        days += md
    md = days_in_month(year, month)
    if day >= 1 and day <= md:
        return days + day
    else:
        return None

print(day_of_year(2000, 12, 31))

# LAB
#  LAB   Prime numbers ‒ how to find them
# A natural number is prime if it is greater than 1 and has no divisors other than 1 and itself.

# Complicated? Not at all. For example, 8 isn't a prime number, as you can divide it by 2 and 4 (we can't use divisors equal to 1 and 8, as the definition prohibits this).

# On the other hand, 7 is a prime number, as we can't find any legal divisors for it.

#  Your task is to write a function checking whether a number is prime or not.

# The function:

# is called is_prime;
# takes one argument (the value to check)
# returns True if the argument is a prime number, and False otherwise.

#   Hint: 
#   Try to divide the argument by all subsequent values (starting from 2) and check the remainder ‒ if it's zero, 
#   your number cannot be a prime; think carefully about when you should stop the process.

# If you need to know the square root of any value, you can utilize the ** operator. 
# Remember: the square root of x is the same as x0.5

#Complete the code in the editor.

#Expected output: 2 3 5 7 11 13 17 19

# SOLUTION
def is_prime(num):
    for i in range(2, int(1 + num ** 0.5)):
        if num % i == 0:
            return False
    return True

for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()


# LAB
# Converting fuel consumption
# A car's fuel consumption may be expressed in many different ways. 
# For example, in Europe, it is shown as the amount of fuel consumed per 100 kilometers.

#In the USA, it is shown as the number of miles traveled by a car using one gallon of fuel.

#Your task is to write a pair of functions converting l/100km into mpg, and vice versa.

#The functions:

#are named liters_100km_to_miles_gallon and miles_gallon_to_liters_100km respectively;
#take one argument (the value corresponding to their names)

#Complete the code in the editor and run it to check whether your output is the same as ours.

Here is some information to help you:

1 American mile = 1609.344 metres;
1 American gallon = 3.785411784 litres.

# Expected output:  60.31143162393162
#                   31.36194444444444
#                   23.52145833333333
#                   3.9007393587617467
#                   7.490910297239916
#                   10.009131205673757

# SOLUTION
# 1 American mile = 1609.344 metres
# 1 American gallon = 3.785411784 litres

def liters_100km_to_miles_gallon(litres):
    gallons = litres / 3.785411784
    miles = 100 * 1000 / 1609.344
    return miles / gallons

def miles_gallon_to_liters_100km(miles):
    km100 = miles * 1609.344 / 1000 / 100
    litres = 3.785411784
    return litres / km100

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))

# Functions and SCOPES
#  The scope of a name (e.g., a variable name) is the part of a code where the name is properly recognizable.
#   e.g the scope of a function's parameter is the function itself.

def my_function():
    print("Do I know that variable?", var)
var = 1
my_function()
print(var)

# how the function interacts with its arguments.
def my_function(n):
    print("I got", n)
    n += 1
    print("I have", n)
var = 1
my_function(var)
print(var)

# Functions with Lists
def my_function(my_list_1):
    print("Print #1:", my_list_1)
    printprint("Print #2:", my_list_2)
    my_list_1 = [0, 1]
    print("Print #3:", my_list_1)
    print("Print #4:", my_list_2)
my_list_2 = [2, 3]
my_function(my_list_2)
print("Print #5:", my_list_2)

# more examples of lists and functions
def my_function(my_list_1):
    print("Print #1:", my_list_1)
    print("Print #2:", my_list_2)
    del my_list_1[0] # Pay attention to this line.
    print("Print #3:", my_list_1)
    print("Print #4:", my_list_2)
my_list_2 = [2, 3]
my_function(my_list_2)
print("Print #5:", my_list_2)

# Global Keyword
#  The global keyword allows you to modify a variable outside of the current scope.
#  Using this keyword inside a function with the name (or names separated with commas) of a variable (or variables), 
#  forces Python to refrain from creating a new variable inside the function ‒ the one accessible from outside will be used instead.

#  e.g. to create a global variable inside a function, you can do this:
def my_function():
    global var #We've added global to the function.
    var = 2
    print("Do I know that variable?", var)
var = 1
my_function()
print(var)


# how it works with lists
def my_function(my_list_1):
    print("Print #1:", my_list_1)
    print("Print #2:", my_list_2)
    my_list_1 = [0, 1]
    print("Print #3:", my_list_1)
    print("Print #4:", my_list_2)
my_list_2 = [2, 3]
my_function(my_list_2)
print("Print #5:", my_list_2)


# Evaluating BMI and converting imperial units to metric units
# assumes that the values of both parameters are always meaningful. It's definitely worth checking if they're trustworthy.
# Ideal thing to do is to check them both and return NONE if any of them looks suspicious.
def bmi(weight, height):
    # the \ (backslash) tells python to continue the line of code in the next line
    if height < 1.0 or height > 2.5 or \
    weight < 20 or weight > 200:
        return None

    return weight / height ** 2

print(bmi(352.5, 1.65)) #Outputs: None


# The code is able to answer the question: 
# What is the BMI of a person 5'7" tall and weighing 176 lbs?

# This is the code we have built:

def ft_and_inch_to_m(ft, inch = 0.0):
    return ft * 0.3048 + inch * 0.0254
 
 
def lb_to_kg(lb):
    return lb * 0.4535923
 
 
def bmi(weight, height):
    if height < 1.0 or height > 2.5 or weight < 20 or weight > 200:
        return None
 
    return weight / height ** 2
 
 
print(bmi(weight = lb_to_kg(176), height = ft_and_inch_to_m(5, 7)))

# Sample functions: Triangles
# Write a function that takes the lengths of the three sides of a triangle as its parameters,
def is_a_triangle(a, b, c):
    if a + b <= c:
        return False
    if b + c <= a:
        return False
    if c + a <= b:
        return False
    return True


print(is_a_triangle(1, 1, 1))
print(is_a_triangle(1, 1, 3))

# Compact version:

def is_a_triangle(a, b, c):
    if a + b <= c or b + c <= a or c + a <= b:
        return False
    return True
 
print(is_a_triangle(1, 1, 1))
print(is_a_triangle(1, 1, 3))

# Triangles and the Pythagorean theorem
def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b

a = float(input('Enter the first side\'s length: '))
b = float(input('Enter the second side\'s length: '))
c = float(input('Enter the third side\'s length: '))

if is_a_triangle(a, b, c):
    print('Yes, it can be a triangle.')
else:
    print('No, it can\'t be a triangle.')

# Pythagorean theorem
def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b
 
def is_a_right_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return False
    if c > a and c > b:
        return c ** 2 == a ** 2 + b ** 2 
    if a > b and a > c:
        return a ** 2 == b ** 2 + c ** 2
print(is_a_right_triangle(5, 3, 4))
print(is_a_right_triangle(1, 3, 4))

# Factorials
# Factorial of a number is the product of all the integers from 1 to that number.
# It's marked with an exclamation mark, and is equal to the product of all natural numbers from one up to its argument.
# 5! = 5 * 4 * 3 * 2 * 1 = 120
# 0! = 1

def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1
 
    product = 1
    for i in range(2, n + 1):
        product *= i
    return product
 
 
for n in range(1, 6): # testing
    print(n, factorial_function(n))

# Fibonacci numbers
# The Fibonacci sequence is a sequence of numbers where each number is the sum of the two preceding numbers.
# The sequence starts with 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817, 39088169, 63245986, 102334155, 165580141, 267914296, 433494437, 701408733, 1134903170, 1836311903, 2971215073, 4807526976, 7778742049, 12586269025, 20365011074, 32951280099, 53316291173, 86267571272, 139583862445, 225851433717, 365435296162, 591286729879, 956722026041, 1548008755920, 2504730781961, 4052739537881, 6557470319842, 10610209857723, 17167680177565, 27777890035288, 44945570212853, 72723460248141, 117669030460994, 190392490709135, 308061521170129, 498454011879264, 806515533049393, 1304969544928657, 2111485077978050, 3416454622906707, 5527939700884757, 8944394323791464, 14472334024676221, 23416728348467685, 37889062373143906, 61305790721611591, 99194853094755497, 160500643816367088, 259695496911122585, 420196140727489673, 679891637638612258, 1100087778366101931, 1779979416004714189, 28
fib_1 = 1 
fib_2 = 1 
fib_3 = 1 + 1  
fib_4 = 1 + 2  
fib_5 = 2 + 3  
fib_6 = 3 + 5  
fib_7 = 5 + 8 

def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
 
    elem_1 = elem_2 = 1
    the_sum = 0
    for i in range(3, n + 1):
        the_sum = elem_1 + elem_2
        elem_1, elem_2 = elem_2, the_sum
    return the_sum
 
for n in range(1, 10): # testing
    print(n, "->", fib(n))

# Recursion
# Recursion is a method of solving a problem where the solution depends on solutions to smaller instances of the same problem.
# A recursive function is a function that calls itself.
def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return n * factorial_function(n - 1)

# Recursion and the Fibonacci sequence
def fib(n):
    if n < 1:
         return None
    if n < 3:
        return 1

    elem_1 = elem_2 = 1
    the_sum = 0
    for i in range(3, n + 1):
        the_sum = elem_1 + elem_2
        elem_1, elem_2 = elem_2, the_sum
    return the_sum

for n in range(1, 10):
    print(n, "->", fib(n))

# Recursive implementation of the factorial function.

def factorial(n):
    if n == 1: # The base case (termination condition.)
        return 1
    else:
        return n * factorial(n - 1)
 
 
print(factorial(4)) # 4 * 3 * 2 * 1 = 24

# Sequence types and mutability
# A sequence is a collection of objects that are stored in a particular order.
# A SEQUENCE is a type of data in Python which is able to store more than one value (or less than one, as a sequence may be empty), 
# and these values can be sequentially (hence the name) browsed, element by element.

# The list is a classic example of a Python sequence

# MUTABILITY − is a property of any Python data that describes its readiness to be freely changed during program execution.
# A mutable object can be changed after it's created.
# An immutable object can't be changed after it's created.

list.append(1)


# A sequence can be mutable or immutable.
# A mutable sequence is a sequence that can be changed after it's created.
# An immutable sequence is a sequence that can't be changed after it's created.

# TUPLE
# A tuple is an immutable sequence type
# A tuple is a sequence of values separated by commas.
# Tuples prefer to use parenthesis ()
# Tuples are immutable, and usually contain a heterogeneous sequence of elements that are accessed via unpacking or indexing

tuple_1 = (1, 2, 4, 8)
tuple_2 = 1., .5, .25, .125

# Using Tuples
# Tuples are used to store multiple items in a single variable.
my_tuple = (1, 10, 100, 1000)

print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[1:])
print(my_tuple[:-2])

for elem in my_tuple:
    print(elem)

# What else can tuples do for you?

# 1. the len() function accepts tuples, and returns the number of elements contained inside;
# 2. the + operator can join tuples together (we've shown you this already)
# 3. the * operator can multiply tuples, just like lists;
# 4. the in and not in operators work in the same way as in lists.
# The snippet in the editor presents them all.

my_tuple = (1, 10, 100)

t1 = my_tuple + (1000, 10000)
t2 = my_tuple * 3

print(len(t2))
print(t1)
print(t2)
print(10 in my_tuple)
print(-10 not in my_tuple)

# One of the most useful tuple properties 
# is their ability to appear on the left side of the assignment operator. 
var = 123
 
t1 = (1, )
t2 = (2, )
t3 = (3, var)
 
t1, t2, t3 = t2, t3, t1
 
print(t1, t2, t3)

# Dictionaries
# The dictionary is another Python data structure.
# A dictionary is a collection of key-value pairs.
# Each key is connected to a value, and you can use a key to access the value associated with that key.

# A dictionary is a mutable data type.
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
phone_numbers = {'boss': 5551234567, 'Suzy': 22657854310}
empty_dictionary = {}
 
print(dictionary)
print(phone_numbers)
print(empty_dictionary)

# How to use Dictionaries
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
phone_numbers = {'boss' : 5551234567, 'Suzy' : 22657854310}
empty_dictionary = {}

# Print the values here.
print(dictionary['cat'])
print(phone_numbers['Suzy'])


# Note:
#  1. if the key is a string, you have to specify it as a string;
#  2.keys are case-sensitive: 'Suzy' is something different from 'suzy'.
#  3.You mustn't use a non-existent key. 
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
phone_numbers = {'boss' : 5551234567, 'Suzy' : 22657854310}
empty_dictionary = {}

# Print the values here.
print(dictionary['cat'])
print(phone_numbers['Suzy'])
print(phone_numbers['president']) # will cause an error

# Keep it vertically aligned
# Example 1:
dictionary = {
              "cat": "chat",
              "dog": "chien",
              "horse": "cheval"
}
# Example 2:
phone_numbers = {'boss': 5551234567,
              'Suzy': 22657854310
}


# Dictionary METHODS & FUNCTIONS
# 1. The keys() method returns a list of all the keys in the dictionary.
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
 
for key in dictionary.keys():
    print(key, "->", dictionary[key]

# 2. The values() method returns a list of all the values in the dictionary.
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

# 3. The items() method returns a list of tuples of key-value pairs in the dictionary.
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
 
for english, french in dictionary.items():
    print(english, "->", french)


# 4. The get() method returns the value for the given key, if present in the dictionary. If not, it returns None (if get() is called with only one argument).
# 5. The pop() method removes the element with the specified key and returns its value.
# 6. The popitem() method removes the last inserted key-value pair from the dictionary.
# 7. The clear() method removes all the elements from the dictionary.
# 8. The update() method updates the dictionary with the elements from the another dictionary object or from an iterable of key-value pairs.
# 9. The setdefault() method returns the value of the item with the specified key. If the key does not exist, insert the key, with the specified value.
# 10. The copy() method returns a shallow copy of the dictionary.
# 11. The fromkeys() method returns a dictionary with the specified keys and value.
# 12. The has_key() method returns true if a dictionary has the specified key, otherwise it returns false.
# 13. The iteritems() method returns an iterator for the dictionary.
# 14. The iterkeys() method returns an iterator for the keys of the dictionary.
# 15. The itervalues() method returns an iterator for the values of the dictionary.
# 16. The viewitems() method returns a view object that displays a list of dictionary's (key, value) tuple pair.
# 17. The viewkeys() method returns a view object that displays a list of all the keys in the dictionary.

# TUPLES & DICTIONARIES
school_class = {}

while True:
    name = input("Enter the student's name: ")
    if name == '':
        break
    score = int(input("Enter the student's score (0-99): "))
    if score not in range(0, 99):
	    break
    if name in school_class:
        school_class[name] += (score,)
    else:
        school_class[name] = (score,) 
for name in sorted(school_class.keys()):
    adding = 0
    counter = 0
    for score in school_class[name]:
        adding += score
        counter += 1
    print(name, ":", adding / counter)

# QUESTION: Complete the code to correctly use the count() method 
# to find the number of duplicates of 2 in the following tuple.

tup = 1, 2, 3, 2, 4, 5, 6, 2, 7, 2, 8, 9
duplicates = # Write your code here.
 
print(duplicates) # outputs: 4

# Solution: 

tup = 1, 2, 3, 2, 4, 5, 6, 2, 7, 2, 8, 9
duplicates = tup.count(2)
 
print(duplicates)

# QUESTION: Write a program that will "glue" the two dictionaries (d1 and d2) together and create a new one (d3).

d1 = {'Adam Smith': 'A', 'Judy Paxton': 'B+'}
d2 = {'Mary Louis': 'A', 'Patrick White': 'C'}
d3 = {}
 
for item in (d1, d2):
    # Write your code here.
 
print(d3)

# Solution: 
d1 = {'Adam Smith': 'A', 'Judy Paxton': 'B+'}
d2 = {'Mary Louis': 'A', 'Patrick White': 'C'}
d3 = {}
 
for item in (d1, d2):
    d3.update(item)
 # Write your code here.
 
print(d3)

# QUESTION: Write a program that will convert the my_list list to a tuple.

d1 = {'Adam Smith': 'A', 'Judy Paxton': 'B+'}
d2 = {'Mary Louis': 'A', 'Patrick White': 'C'}
d3 = {}
 
for item in (d1, d2):
    # Write your code here.
 
print(d3)

# Solution:
d1 = {'Adam Smith': 'A', 'Judy Paxton': 'B+'}
d2 = {'Mary Louis': 'A', 'Patrick White': 'C'}
d3 = {}
 
for item in (d1, d2):
    
    my_list = ["car", "Ford", "flower", "Tulip"]

t = tuple(my_list)
print(t)
print(d3)

# QUESTION: Write a program that will convert the colors tuple to a dictionary.

colors = (("green", "#008000"), ("blue", "#0000FF"))
 
# Write your code here.
 
print(colors_dictionary)

# Solution:
colors = (("green", "#008000"), ("blue", "#0000FF"))
colors_dictionary = dict(colors)
print(colors_dictionary)

# EXCEPTIONS
# Man is to err - It's impossible to make no mistakes, and it's impossible to write error-free code. 

value = int(input('Enter a natural number: '))
print('The reciprocal of', value, 'is', 1/value)

# The try-except branch

try:
	# It's a place where
	# you can do something 
    # without asking for permission.
except:
	# It's a spot dedicated to 
    # solemnly begging for forgiveness.

# Solved
try:
    value = int(input('Enter a natural number: '))
    print('The reciprocal of', value, 'is', 1/value)        
except:
    print('I do not know what to do.')


# Two exceptions after one try
try:
    value = int(input('Enter a natural number: '))
    print('The reciprocal of', value, 'is', 1/value)        
except ValueError:
    print('I do not know what to do.')    
except ZeroDivisionError:
    print('Division by zero is not allowed in our Universe.') 
# second except branch is introduced and both branches have exception names specified
# if one of the branches is executed, all the other branches remain idle.

# The default exception

# added a third except branch, but this time it has no exception name specified – we can say it's anonymous
# it will be executed only if the first two branches are not executed
try:
    value = int(input('Enter a natural number: '))
    print('The reciprocal of', value, 'is', 1/value)        
except ValueError:
    print('I do not know what to do.')    
except ZeroDivisionError:
    print('Division by zero is not allowed in our Universe.')    
except:
    print('Something strange has happened here... Sorry!')

# Other Useful Exceptions

# 1. ZeroDivisionError
#  This appears when you try to force Python to perform any operation which provokes division in which the divider is zero

# 2. TypeError
#  This appears when you try to force Python to perform any operation which provokes division in which the divider is zero

# 3. IndexError
#  This appears when you try to force Python to perform any operation which provokes division in which the divider is zero

# 4. KeyError
#  This appears when you try to force Python to perform any operation which provokes division in which the divider is zero
short_list = [1]
one_value = short_list[0.5]
