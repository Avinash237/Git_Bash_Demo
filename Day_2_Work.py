Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# identifiers: names given to the objects
100
100
200
200
'python'
'python'
# above all are the objects
x = 100
# 100 is an object and x is identifier
y= 'python'
# y  is an identifier
# how to check memory address of an address
id(x)
140737128027672
id(y)
2246522682560
#===============================

# ruels of identifiers
# a-z alphabates are allowed
# words allowed
info = 'Pune'
info
'Pune'
#_ underscore are allowed
_a = 'Good evining'
_a
'Good evining'
_ = 5000
_
5000
# Space is not allowed
bank pin = 1234
SyntaxError: invalid syntax
# _ will help to make it valid
bank_pin = 1234
bank_pin
1234
# special symbols and characters are not valid vfor idetifiers
@ = 'Sham'
SyntaxError: invalid syntax
# reserved keywords are not valid
int = 'income'
in = 'income'
SyntaxError: invalid syntax
# numbers are not valid
4 = 400
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
# number in prefix is not valid
2x = 500
SyntaxError: invalid decimal literal
x2 = 400
x2
400
# operators in python
# Arithmatic operator : + - * / % // **
# Arithmatic operator : + - * / % // **
a + 8
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    a + 8
NameError: name 'a' is not defined. Did you mean: '_a'?
1+8
9
9-8
1
45/5
9.0
# mod: % returns remainder
45//5
9
# floor division
# 12(floor).55(ceil)
10/3
3.3333333333333335
10//3
3
# power of operator/exponential
2 ** 8 # 2 is a number and 8 is a power
256
3**3 # cube
27
3**21
10460353203
#========================================================
d = 80
d
80
d + 100
180
d += 100
d
180
d -= 100
d
80
d -= 40
d
40
d /= 7
d
5.714285714285714
d
5.714285714285714
d *= 2
d
11.428571428571429
d **= 3
d
1492.7113702623908
# comparison / conditional / relational operators
# < > <= >= == !=
# it returns boolean output
#(True,False)
3 > 2
True
4 >=2
True
'Amit' == 'amit'
False
4! = 5
SyntaxError: invalid syntax
4 != 5
True
# = (Assignment) & == (comparison)
#=========================================

# Membership: we check the object is a member or not
# in, not in
'suyash' in 'suyash pawar'
True
12 in [2,4,6,8]
False
# if object is present it returns True else False
# identity operator
# returns boolean value and it check identity of an object
# meanse if ids of both objects are same thrn those objects are same
# id meanse address
# if address are same then True else false
'python' is 'python'
True
id('python')
2246522682560
'Python' is 'python'
False
id('Python')
140737126912800
id('python')
2246522682560
d1 = [1,2,3,4]
d1
[1, 2, 3, 4]
d2 = d1
d2
[1, 2, 3, 4]
d1 is d2
True
id(d1)
2246560580800
id(d2)
2246560580800
d2.append(100)
d2
[1, 2, 3, 4, 100]
d1
[1, 2, 3, 4, 100]
# ===========================
# logical operators
>>> # it returns boolean output
>>> 1 and 1
1
>>> 1 and 0
0
>>> 2 and 4
4
>>> 4.9 and 11
11
>>> name = 'aditi'
>>> name
'aditi'
>>> palce = 'pune'
>>> palce
'pune'
>>> palce = 'mumbai'
>>> name =='swati' and palce == 'pune'
False
>>> name =='swati' and palce == 'mumbai'
False
>>> name = 'aditi'
... >>> name
... 'aditi'
... >>> place = 'pune'
... >>> place
... 'pune'
... >>> name=='swati'
... False
... >>> place == 'mumbai'
... False
... >>> name=='swati' and place == 'mumbai'
... False
... >>> name=='swati' and place == 'pune' # 0 1
... False
... >>> name=='aditi' and place == 'Une' #1 0
... False
... >>> name=='aditi' and place == 'pune' #1 1
... True
SyntaxError: multiple statements found while compiling a single statement
