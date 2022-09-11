""" Abstract Base Classes

"""

"""
Abstract base classes are classes whose methods are defined but not implemented. They cannot be instantiated, and 
need to be overidden by subclasses that are using the abc class.

A class derived from an abstract class cannot be instantiated unless all the abstract methods are defined for the 
derived class. We can mark methods which we 'need' to be defined by the user when he is inheriting from the abstract
base class by using the decorator `@abstractmethod`. 

It is still possible to invoke methods defined in the abc definition without having to fully write a new method in the 
derived class. For example, some of the implementation of the abc can be transferred to the derived class by using the 
`super()` keyword as shown below.
"""

from abc import ABC, abstractmethod

class AbstractClass(ABC):

    @abstractmethod
    def do_something(self):
        print(f'I need to do something')

class NewClass(AbstractClass):

    def do_something(self):
        super().do_something()
        print(f'I do something more')

x = NewClass()
x.do_something()
print(x)
