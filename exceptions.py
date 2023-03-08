value = int(input('Enter a natural number: '))
print('The reciprocal of', value, 'is', 1/value)

# Inputing a float returns a "ValueError: invalid literal for int()"

# Solved
try:
    value = int(input('Enter a natural number: '))
    print('The reciprocal of', value, 'is', 1/value)        
except:
    print('I do not know what to do.')
