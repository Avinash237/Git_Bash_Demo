"""

"""

"""
function: a single unit of a program which is declare ones and used/call multiple times
"""
#------------------------------------------------
"""
    There are 2 steps
    - Declaration 
    syntax:
    def func_name():
        pass
        
    - Calling
    syntax:
    fucn_name()        

-----------------------------------------------------------------------
    2 Types 
    - Built-in function 
    ex. print,help,dir()....
    - user defined function 
    
    
----------------------------------------------------------------
def calc():
    a = 10
    b = 20
    print('Addition is:',a + b)
    print('Substaction is: ',a - b)

# calling means actually executs a function
calc()

# Advantage: Code Resusality
--------------------------------------------------


# supply value to func
def calc(a,b):
    print('Addition is:',a + b)
    print('Subtraction is:',a - b)
calc(40,20)
# we can supply othe value too
calc(99,77)

------------------------------------------------------------
# supply value at runtime
def calc(a,b):
    print('Addition is: ',a + b)
    print("Subtraction is: ", a - b)

for i in range(3):
    val1 = int(input('Enter the first number: '))
    val2 = int(input('Enter the second number: '))
    calc(val1,val2)

    """