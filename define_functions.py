# Defineing a function and applying it to a simple greeting program
def greet(name):    # defining a function
    print("Welcome,", name)    # body of the function
def living_country(country):
    print(country ," is in the house! Yipee!")

name = input("Enter your name: ")
country = input("Where do you live? : ")

greet(name)    # calling the function
living_country(country)
