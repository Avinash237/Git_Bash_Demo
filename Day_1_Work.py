Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# python intruduction
# 'hash' is used for single line comment purpose
print('Welcome Python')
Welcome Python
print(9568321569)
9568321569
# currently python 3.13 version is going on
# python is open source
# Huge community support
#simple and easy to use
list (range(2,21))
[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# generate 2-20 even numbers
list(range(2,21,2))   # jump by 2
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
n = "Python World"
n
'Python World'
n.upper()
'PYTHON WORLD'
n.title()
'Python World'
n.[::1]
SyntaxError: invalid syntax
n[::]
'Python World'
n[[::1]
  
SyntaxError: invalid syntax
n[::1]
  
'Python World'
n.[::-1]
  
SyntaxError: invalid syntax
n[::-1]
  
'dlroW nohtyP'
# python support 14 data structurs
  

#python support 35 keywords
  
# data structures
  
# numeric: int,float,complex
  
#int 0-9 values
  
13
  
13
#float : decimal point
  
2.3
  
2.3
3.14
  
3.14
# complex : real + img
  
3+4j
  
(3+4j)
int a = 22  # static typing
  
SyntaxError: invalid syntax
#int a = 22
  
# python supports dynamic typing
  
x = 10
  
x
  
10
y = 4.55
  
z = 4+5j
  
# to check type of any veriable type()
  
type(x)
  
<class 'int'>
type(y)
  
<class 'float'>
type(z)
  
<class 'complex'>
# boolean : True False
  
True
  
True
False
  
False
# python is case sensetive language
  
2 > 4
  
False
3 == 3
  
True
'Well' = 'well'
  
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
'Well' == 'well'
  
False
# while comparing the object we get boolean output
  
# string
  
#syntax : '' ""
  
a = 'python'
  
type(a)
  
<class 'str'>
<class 'str'>
  
SyntaxError: invalid syntax

s = "999"
  
s
  
'999'
type(s)
  
<class 'str'>
# List
  
# systex
  
#Syntax
  
[]
  
[]
# empty list
  
type([])
  
<class 'list'>
v = [3,4,5,77,6934]
  
v
  
[3, 4, 5, 77, 6934]
# list is the collection of element
  
# Tuple
  
# Syntax: ()
  
()
  
()
type(())
  
<class 'tuple'>
empty tuple
  
SyntaxError: incomplete input
t = (7,8,9,'go','stop')
  
t
  
(7, 8, 9, 'go', 'stop')
type(t)
  
<class 'tuple'>
# set:
  
#syntax: {1, }
  
s = set()
  
s
  
set()
set()
  
set()
>>> # empty set
...   
>>> p = {}
...   
>>> type(p)
...   
<class 'dict'>
>>> # empty  {} is not set it is dict
...   
>>> # dict
...   
>>> # syntax: {key:value}
...   
>>> {}
...   
{}
>>> t = {10:1,20:2,30:30}
...   
>>> t
...   
{10: 1, 20: 2, 30: 30}
>>> y= {'a':'apple','b':'ball'}
...   
>>> y
...   
{'a': 'apple', 'b': 'ball'}
>>> y['a']
...   
'apple'
>>> # null/nothing
...   
>>> # keywords: Reserved words in python
...   
>>> import keyword
>>> print(keyword.kwlist)
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> len(keyword.kwlist)
35
