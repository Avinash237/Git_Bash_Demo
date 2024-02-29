Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Q.    use remove and replace
>>> # Q.    use remove and replace
>>> s1 = '  Welcome    Home    '
>>> s1
'  Welcome    Home    '
>>> s1.strip()
'Welcome    Home'
>>> s.replace(' ','')
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    s.replace(' ','')
NameError: name 's' is not defined. Did you mean: 's1'?
>>> s1.replace(' ','')
'WelcomeHome'
>>> s2 = '####shaktiman****'
>>> s2
'####shaktiman****'
>>> s2.remove('#')
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    s2.remove('#')
AttributeError: 'str' object has no attribute 'remove'
