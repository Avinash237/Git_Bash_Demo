"""
Flow control blocks-
iterative statement

for loop

for var_name in iterable:
    process


-----------------------------------------------"""
# pattren program on for loop
"""
*
**
***
****
*****



for i in range(0,5):
    print(i*"*")
------------------------------------------------------------

*****
*****
*****
*****
*****

for i in range(0,5):
    print("*"*4)
    
-----------------------------------------------------------    
 

for i in range(5):
    print("ur name")

# Capital alphabet sart from 65
for i in range(1,5): # 1,2,3,4
    print(chr(65+i)*i)
    
----------------------------------------------------------------

for i in range(1,5):
    for j in range(1,5):
        #print(chr(101-j),end='')
        print(chr(101 - i),end='')
    print()
    
---------------------------------------------------------------------

for i in range(1,5):
    for j in range(i+1):
        #print(' '*i+chr(101-j),end='')
        print(' '*i+chr(101 - i),end='')

    print()
    
-------------------------------------------------------------
"""
# While loop
"""
Conditional infinite loop
syntax:
    while <condition>
    


-------------------------------------------------------------------
num = 8

while num>2:
    print("Hello")
    num-=1
# programer has to writ a logic
# which can make the condition result false
--------------------------------------------------------------------

# print 'python' 5 times

count = 1
while count<=5:
    print("Python")
    count += 1
    
-----------------------------------------------------------------------    

k = ['aditi','tejas','deepa','siddhesh']
# we need 0-3 index as we have 4 element
index = 0
while index  < 4:
    print(k[index])
    index += 1
---------------------------------------------------------------------------
"""

for i in range(1,5):
    for j in range(i+1):
        #print(' '*i+chr(101-j),end='')

        print(' '*i+chr(101 - i),end='')


    print(" ")