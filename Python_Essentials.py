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

#Once upon a time in Appleland, John had three apples, Mary had five apples, and Adam had six apples. They were all very happy and lived for a long time. End of story.

#Your task is to:

#1. create the variables: john, mary, and adam;
#2. assign values to the variables. The values must be equal to the numbers of fruit possessed by John, Mary, and Adam respectively;
#3. having stored the numbers in the variables, print the variables on one line, and separate each of them with a comma;
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

#

