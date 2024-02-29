"""
-   Abstraction:
"""
"""
    Abstarction mense information hiding
    - for abstarction we need to perform 2 tasks\
    1. inheerit ABC class in normal class
       ABC(Abstarct base class) class we can import from abc module
       
    2. rule: abstarct class should have atleast onr abstarct method
      -  a normal method can be converted to abstarct using abstact method decorator
      -  we have to import abstarctmethod decorator form abc 

from abc import ABC, abstractmethod
class RBI(ABC):

    def information(self):
        print('RBI Information..')

    @abstractmethod
    def security(self):
        print('RBI Security')

    @abstractmethod
    def protocols(self):
        pass

# after pure abstarction we wont be able to create an object of an abstarct class
# we dont access security and protocols mehtod using RBI class object
#rb = RBI()  # it will give an error

class SBI(RBI):
    def security(self):
        print('SBI policies with ref to RBI')
        super().security()

    def protocols(self):
        print('SBI folows RBI protocols')

sb = SBI()
sb.security()

---------------------------------------------------------------------------
"""








































