""" Factory Pattern

his pattern works with object creation, and is thus a creational design pattern
"""

"""
This method abstracts away the object creation part from the object calls via a `factory method`. 

Objects returned by a factory are called `products`


We usually have a creator class, which acts as a factory class, and the product subclasses inheriting from the creator
class can override the abstract method that is defined. 

We should use the factory method when we don't know what types of objects we will be working with, and since the 
creation of the object is abstracted away from the usage of the object, we can add more object types later.

Example of factory method in Python
"""

from abc import ABC, abstractmethod


class Creator(ABC):

    @abstractmethod
    def factory_method(self):
        pass

    def business_logic(self):
        product = self.factory_method()
        result = f'The creator code has worked with {product.operation()}'


class ConcreteCreator1(Creator):

    def factory_method(self):
        return ConcreteProduct1()


class ConcreteCreator2(Creator):

    def factory_method(self):
        return ConcreteProduct2()


class Product(ABC):

    @abstractmethod
    def operation(self):
        pass


class ConcreteProduct1(Product):

    def operation(self):
        return f'I am from Concrete Product 1'


class ConcreteProduct2(Product):

    def operation(self):
        return f'I am from Concrete Product 2'


def client_code(creator):
    print(f'The creator object does not have any of the objects that we had created, and yet it is able to access'
          f'the function operation from inside the {creator.business_logic()} from the class')


client_code(ConcreteCreator1())

#################################

"""
Another example showing the factory design. We could have two language localizers and decide during execution which 
objects localize method will be called.
"""


class HindiLocalizer:
    def __init__(self):
        self.translations = {'dog': 'kutta', 'cat': 'billi'}

    def localize(self, msg):
        return self.translations.get(msg, msg)


class EnglishLocalizer:

    def localize(self, msg):
        print(f'This is english, so returning the same statement')
        return msg


def get_localizer(language):
    localizers = {
        'hindi': HindiLocalizer(),
        'english': EnglishLocalizer()
    }

    return localizers[language]


e_localizer = get_localizer('english')
h_localizer = get_localizer('hindi')

for word in ["dog", "cat"]:
    print(e_localizer.localize(word))
    print(h_localizer.localize(word))

"""
In a simple description, we define the creation of the objects in a different function, rather than in the main class
or during execution directly. This helps avoid using `if-else` statements.
"""