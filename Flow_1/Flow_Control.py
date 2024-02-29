"""

It is multiline comment
also known as multilne doctring.

"""

"""
- Flow controll block have 3 types
- 1. Selective/condition statments
    - used for selection/performing the operation based on condition
    
    - if condition is True then perform operation otherwise exit
    
    
    - syntax:
        - if <condition>:
        - # execute process_1 if condition is True
 

------------------------------------------
# perform operation if number is +ve

num = -2
if num >= 0:
    print("Number is +ve")
-------------------------------------------

-----------------------------------------------
# for placement required per > 60

per = 59
if per > 60:
    print("Allowed for campus placement")
else:
    print("Not Allowed")
    
----------------------------------------------------    

# we can use else to go for alternate option

# else follows if: means if condion is flase then automatically else block will get executed

# if if condition ased else id condition less
#------------------------------------------------------------------
#if we want to test multiple condition then we use elif <condition>
----------------------------------------------------------------
amt = 80000

if amt >= 100000:
    print("you can buy iPhone")
elif amt >= 70000:
    print("you can buy Vivo")
elif amt >= 40000:
    print("you can buy Realme")
elif amt >= 10000:
    print("you can buy MI")
else:
    print("Dont buy phone, buy choclate")
----------------------------------------------------------------------
# tack an input from user
amt = (float)(input("Enter the Number: "))

print("Amount:",amt)
print(type(amt))

# as input default data type is str
# hence it is needed to convrt into int/float

------------------------------------------------------------------------
"""

amt = (int)(input("Enter the Amount: "))
print("Amount: ",amt)
if amt>= 100000:
    print('You can purchase iPhone')
elif amt>=50000:
    print('You can purchase RealMe/Vivo')
elif amt>=40000:
    print('You can purchase MI')
else:
    print('You can purchase Any other Cell Phone')

    




