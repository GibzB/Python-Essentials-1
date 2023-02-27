# Sample functions: Evaluating the BMI

# BMI function will have two parameters
# 1. weight in kilograms
# 2. height in meters

def bmi(weight, height):
    return weight / height ** 2

print(bmi(52.5, 1.65))