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
