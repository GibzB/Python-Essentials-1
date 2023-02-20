# Shadowing in Python occurs when a variable or function with the same name 
# as an existing variable or function is defined within a more nested scope. 
# 
# This can lead to unexpected behavior as the inner variable or function will "shadow" the outer one, 
# making it inaccessible or causing the code to behave differently than intended.
def message(number):
    print("Enter a number:", number)
 
number = 1234
message(1)
print(number)