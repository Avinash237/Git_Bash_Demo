"""
Flow controll blocks
    1. conditional and selective statement
    if <condition>
    if else
    if elif else
    if elif elif .... else
"""
"""

-----------------------------------------------
# check number is divisible by 5
num = 59
if num%5 == 0:
    print("Acccept")
else:
    print("Reject")
    
 -------------------------------------------------------
 
-------------------------------------------------
# check number is divisible by 5 and 7
num = 35

if num%7 == 0 and num%5 == 0:
    print('Accept')
else:
    print("reject")
 -----------------------------------------------------   
 
---------------------------------------------------
# Nested if: if inside if


temp = 83
rtpcr = True

if rtpcr == True:
    if temp > 90:
        print("Admit the patient")
    else:
        print("Home isolation")
else:
    print("Go Home")
    
 ----------------------------------------------   
"""

# Iterative statement
"""
1. for loop
2. while loop

# for loop: is used to fetch elements from an iterable one by one
# iterable in python: list,set,tuple,dict,range

s = [100,34,55,78,90,120]
# for va_name is iterable 's':
for num in s:
    print(num,end='\n')


---------------------------------------------------------------------

s = [100,34,55,78,90,120]
for num in s:
    if num%2!= 0:
        print("odd number is: ",num)
    else:
        print("even numer is: ",num)
-----------------------------------------------------------------------------

# display seprate list of +ve and -ve

list1 = [11,-22,33,-44,55,-66,77,-88,99]
pn = []
nn = []
for num in list1:
    if num < 0:
        pn.append(num)

    else:
        nn.append(num)

print("negative number list =",pn )
print("positive number list =", nn)


--------------------------------------------------------------------------------------------


# write a program to findout n display numbers/code only
str1 = "hello ankit i m sending the code 45678 and other one is 76589"
for i in str1.split():
    if i.isdigit():
        print(i)
----------------------------------------------------------------------------------------------
"""