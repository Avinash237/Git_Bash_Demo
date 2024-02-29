Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# Builtin function from python
print()

# print(object,sep=' ',end='\n')
print(10,20,30)
10 20 30
# instead of space
print(10,20,30,sep='-')
10-20-30
print(10,20,30,sep='\n')  # \n = new line
10
20
30
print(10,20,30,sep='\t')  # \t tab with 4 space
10	20	30
# we can work on end
print(' I am 23', end='years old')
 I am 23years old
print(end='\n\n')


print("Hello Good Evinin Pythoniest")
Hello Good Evinin Pythoniest
print('Hello \nGood Evining \nPythoniest')
Hello 
Good Evining 
Pythoniest
print("Hello");print('GE')
Hello
GE
#====================================
f = [10,20,30,40]
f
[10, 20, 30, 40]
# doaddition of all numbers
sum(f)
100
# find max sum
max(f)
40
# count total elements present in the element
reversed(f)
<list_reverseiterator object at 0x000001C289970C40>
# object we need to convert
list(reversed(f))
[40, 30, 20, 10]
# temp
f
[10, 20, 30, 40]
# to sort we can use sorted()
sorted(f)
[10, 20, 30, 40]
sorted([100,7,18,5,0,150])
[0, 5, 7, 18, 100, 150]
# default sorting is in ascending order
sorted([100,7,18,5,0,150],reversed = True)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    sorted([100,7,18,5,0,150],reversed = True)
TypeError: 'reversed' is an invalid keyword argument for sort()
sorted([100,7,18,5,0,150],reverse = True)
[150, 100, 18, 7, 5, 0]
#reverse= True will make it in decending order
#================================================
# typcasting; conversion of a data
d = '100'
d
'100'
# d is of str type
a + 100
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    a + 100
NameError: name 'a' is not defined
d + 100
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    d + 100
TypeError: can only concatenate str (not "int") to str
int(d) + 100
200
float(d)
100.0
list(d)
['1', '0', '0']
# inplicite typecasting: performed by python
3 + 4 + 1.
8.0
3 + 4 + 1
8
# int --> float --> complex
10/2
5.0
# explicite typecasting: conversion by user
int(10/2)
5
complex(10/2)
(5+0j)
# problems with data types
100 + 100
200
'100' + '100'
'100100'
 3 * 4
 
SyntaxError: unexpected indent
3 * 4
12
3 * '4'
'444'
7 * '4'
'4444444'
# 4 repeated 7 times
3 * int'4'
SyntaxError: invalid syntax
3 * int('4')
12
#======================================
# string Data Type
# features of string
# string is a global acceptor: Accept All typee of data
# store a data in sequential order
# background data structure is an array
s = 'Sachin Tendulkar'
s
'Sachin Tendulkar'
# each character is one block
# we can fetch single char using an index
# index start with 0
# and stop at (n-1)
len(s)
16
>>> s[0]
'S'
>>> s[5]
'n'
>>> #index gives an acess to single char
>>> s
'Sachin Tendulkar'
>>> # s[start:stop]
>>> #fetch sachin
>>> s[:6]
'Sachin'
>>> # default start with 0
>>> s[7:]
'Tendulkar'
>>> s[7:10]
'Ten'
>>> # python has -ve indexing
>>> s[15]
'r'
>>> s[-1]
'r'
>>> s[-16]
'S'
>>> s[-3:]
'kar'
>>> # want in reverse
>>> s[-1:-4]
''
>>> s[-1:-4-1]
''
>>> #reverse the string
>>> s[::-1]
'rakludneT nihcaS'
>>> # while reversing it start reading from right side
>>> s[:6]
'Sachin'
>>> s[:6][::-1]
'nihcaS'
