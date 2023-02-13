values = []

# get number of values from user
num_values = int(input("How many values would you like to enter? "))

# loop through and get values from user
for i in range(num_values):
    value = input(f"Enter value {i + 1}: ") 
# The "f" in "f" in "input(f"Enter value {i + 1}: ")" is short for "format". 
# It allows for string interpolation, where values can be incorporated into a string by wrapping the string in curly braces {} and prefixing it with "f"
    values.append(value)

print(values)