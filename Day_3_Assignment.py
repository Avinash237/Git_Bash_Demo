Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# Q. +ve and -ve indexing each 10 examples
str = "To select numbers from the end of the list, we use negative indexes starting from -1 and adding -1 each time to get the next number from the end"
str
'To select numbers from the end of the list, we use negative indexes starting from -1 and adding -1 each time to get the next number from the end'
str[:10]
'To select '
str[11:10:2]
''
>>> str[5:8:3]
'l'
>>> str[2:13]
' select num'
>>> str[:12]
'To select nu'
>>> str[::-1]
'dne eht morf rebmun txen eht teg ot emit hcae 1- gnidda dna 1- morf gnitrats sexedni evitagen esu ew ,tsil eht fo dne eht morf srebmun tceles oT'
>>> str[-6:-6]
''
>>> str[-9:6]
''
>>> str[-11:11]
''
>>> str[-12:3]
''
>>> 
>>> 
>>> 
>>> # Q2.   +ve and -ve slicing each 10 example
>>> str1 = "With the help of negative indexes, we do not need to know the exact size of the sequence objects to retrieve elements placed at the end of the list"
>>> str1
'With the help of negative indexes, we do not need to know the exact size of the sequence objects to retrieve elements placed at the end of the list'
>>> str1[3::6:9]
SyntaxError: invalid syntax
>>> str1[3:9:1]
'h the '
>>> str1[9:1:11]
''
>>> str1[11:6]
''
>>> str1[10:9]
''
>>> str1[9:-1]
'help of negative indexes, we do not need to know the exact size of the sequence objects to retrieve elements placed at the end of the lis'
