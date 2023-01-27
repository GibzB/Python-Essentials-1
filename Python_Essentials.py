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

# Inequality: the not equal to operator (!=)


# Comparison operators: greater than or equal to (>=)

# Comparison operators: less than (<)

# Comparison operators: less than or equal to (<=)