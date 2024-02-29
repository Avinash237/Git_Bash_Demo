"""
Modules:
"""
"""
-   a python file is a module
-   if file present in project folder then we can access members directly 
-   but file present in another folder/s then we have to follow hirarchycal path  


import Sample
#print(dir(Sample))
Sample.show_info('Avinash','Pune')
# use name and place from sample
Sample.show_info(Sample.nm,Sample.place)
--------------------------------------------------------
Modules are 2 types
-   Builtin modules
-   user-define modules

import math
print(math.e,math.pi)
--------------------------------------


#Module alising

import math as m
# import
from math import pi,sqrt
# now member are directly available
print(pi,sqrt(225))


print(help('modules'))
-------------------------------------------------
"""



















