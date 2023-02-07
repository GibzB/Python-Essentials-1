x = 15
y = 16
mask = 8
flag_register = 0000000000000000000000000000x000


x & y
x | y
~ x 
x ^ y 
y >> 1
y << 3 # 

flag_register = flag_register & ~mask
flag_register &= ~mask

if flag_register & mask:
    # My bit is set.
    print("Done")
    else:
    # My bit is reset.
