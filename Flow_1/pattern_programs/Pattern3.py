"""
5432112345
5432 2345
543  345
54   45
5     5
"""

rows = 6
for i in range(0,rows):
    for j in range(rows -1, i, -1):
        print(j,'',end="")
    for I in range(i):
        print("    ",end="")
    for k in range(i + 1,rows):
        print(k,'',end='')
    print('\n')

