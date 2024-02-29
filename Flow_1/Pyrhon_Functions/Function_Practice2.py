"""
function


"""
"""
#function with return:
return: it is a keyword used in function to bring the value/object from inside the function to outside
----------------------------------------------------------------
def operation(x,y):
    #print(x * y)
    return x * y
result = operation(22,44)
print(result)
------------------------------------------------------------------------------------

# can we return multiple object --> YES
def operation(x,y):
    expr = x*y,x**y,x+100
    return expr
result = operation(22,44)
print(result)
-----------------------------------------------------------------------------


def operation(x,y):
    expr = x*y,x**y,x+100
    return expr
result = operation(22,44)
#print(result)
x1,x2,x3 = operation(10,2)
print(x1,x2,x3)
-----------------------------------------------------------------------


# in string we have some methods those have return
s = 'Demo Lecture'
i = s.index('Lec')
print(s[i:])
--------------------------------------------------------


# show directly
s = 'Demo Lecture'
print(s.index('Lec'))
-----------------------------------------
"""
""""
Function Argument/parameters
There are 4 types 
    - positional argument
    - keyword argument
    - default argument
    - varible lenght argument    

"""
"""
------------------------------------------------------
1. Positional: in which sequence order of matters
Ex.
def details(day,month,year):
    print('Day: ',day)
    print('Month: ',month)
    print('Year: ',year)
details(12,4,2016)
#details(2016,23,88)   # wrong calling/pramers
    # if we change the sequence then it will give wrong allocation
    # in the same order we have to give values
------------------------------------------------

# above problem gets solved by keyword arguments
2.  Keyword args:
ex:

def details(day,month,year):
    print('Day',day)
    print('Month',month)
    print('Year',year)
details(16,'Feb',2024)  # positional
#use kayword argument
details(year=2024,day=22,month=2022)
--------------------------------------------------------------

3.  Default args: we use declaration

def account(name="gust_name",branch="ICICI"):
    print("Name is",name)
    print('brach is',branch)
account()   # it takes default arguments
print('-------------------------')
account('Narayan','ICICI Ktraj')
print('---------------------------')
account(branch='SBI')


------------------------------------------------------
4.  veriable lengh arguments:
    - positional var. len: *args
    
    - supplying var length args through function calling is not allowed
    
---------------------------------------------------------------------
def numbers(n):
    print(n)
numbers(1)
numbers(4,8,6)
numbers()
numbers(1,2,3,4,5,6)


---------------------------------------------------
# the solution of above problem is *n
def numbers(*n):
    print(n)
numbers(1)
numbers(3,4,6)
numbers()
numbers(1,2,'ajit','seema')
------------------------------------------------------------
-   keyword var len: **kwargs
eg.

def numbers(**kwargs):
    print(kwargs)
numbers(name = 'Python')
numbers(name='Ketan',age=33)
numbers()
---------------------------------------------------------------
-   laambda function also called anonymous/nameless function
- it is a short representation of a function

syntax:
lambda parameter/s:express

lambda - keyword
- we can supply arguments and parametes 
- we can give only one expression 
- lambda function has default return
- eg 

convert = lambda name:name.upper()
print(convert('Sachine'))
print(convert)
--------------------------------------------------

def add(x,y):
    return x + y,x - y
print(add(4,8))

ad = lambda x,y:(x+y,x-y) # only one expression is called that why we used ()
print(ad(80,99))
-----------------------------------------------------------------------------
"""


