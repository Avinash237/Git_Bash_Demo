Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# string Method
#"".
"".
SyntaxError: incomplete input
dir('')
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
help(str.split)
Help on method_descriptor:

split(self, /, sep=None, maxsplit=-1)
    Return a list of the substrings in the string, using sep as the separator string.

      sep
        The separator used to split the string.

        When set to None (the default value), will split on any whitespace
        character (including \n \r \t \f and spaces) and will discard
        empty strings from the result.
      maxsplit
        Maximum number of splits (starting from the left).
        -1 (the default value) means no limit.

    Note, str.split() is mainly useful for data that has been intentionally
    delimited.  With natural text that includes punctuation, consider using
    the regular expression module.

>>> ip = '198.162.10.109'
>>> ip
'198.162.10.109'
>>> ip.split('-')
['198.162.10.109']
>>> ip.split()
['198.162.10.109']
>>> nm = 'sham shivam pawar'
>>> nm
'sham shivam pawar'
>>> nm.upper()
'SHAM SHIVAM PAWAR'
>>> nm.title()
'Sham Shivam Pawar'
>>> nm.capitalize()
'Sham shivam pawar'
>>> nm.lower()
'sham shivam pawar'
>>> a = 'AviNAsh'  # convert upper to lower and vice versa
>>> a.swapcase()
'aVInaSH'
>>> # replace(old,new)
>>> nm.replace('pawar','patil')
'sham shivam patil'
>>> # when we want to remove spaces in prefix and suffix then use strip()
>>> d = '   Gayatri    '
>>> d
'   Gayatri    '
>>> d.strip()
'Gayatri'
>>> # to remove all spaces use replace
>>> # strip only works in prefix and suffix
