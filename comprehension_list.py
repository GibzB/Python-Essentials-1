# list comprehension is actually a list, but created on-the-fly during program execution, and is not described statically.


WHITE_PAWN = "-8-"
KNIGHT = "-$-"

row = [WHITE_PAWN for i in range(8)]
row7 = [KNIGHT for i in range(8)]


print(row)
print(row7)