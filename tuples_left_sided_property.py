var = 456
 
t1 = (4, )
t2 = (5, )
t3 = (6, var)
 
t1, t2, t3 = t2, t3, t1
 
print(t1, t2, t3)