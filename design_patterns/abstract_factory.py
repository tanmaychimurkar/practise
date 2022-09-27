""" Abstract Factory

This is a creational design pattern that abstracts away the creation of an object via factory classes.
"""

"""
We can use this design when we do not know beforehand which type of objects we will be dealing with. All objects follow
an interface, and all the methods of the interface are overridden by the subclasses. 

Note: The base factory in this case is a interface, not an abstract class. Abstract classes may have default methods
defined for them, but interfaces have no default methods defined, and is `literally` an interface of what methods should
the inheriting class have.

The factory in this case that is defined is a type of `factory that produces objects`
"""


class Pet():

    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplemented

    def __str__(self):
        raise NotImplemented


class Dog(Pet):
    def speak(self):
        return "Woof"

    def __str__(self):
        return f'I am your Dog {self.name}'


class Cat(Pet):
    def speak(self):
        return "meow"

    def __str__(self):
        return f'I am your Cat {self.name}'


"""
So far, we have defined Dog and Cat classes that inherit from the interface `Pet`. We can now initialize the dog and 
cat classes as follows:

my_dog = Dog('Spike')
my_cat = Cat('Tom')

we can also now call the methods speak for both these objects. But in this way, the objects are created everytime a new
instance is to be created for either the cat or the dog. We can use a abstract factory that will create the objects for 
us instead
"""


class PetShop():

    def __init__(self, animal_factory):
        self.pet_factory = animal_factory

    def buy_pet(self, name):
        pet = self.pet_factory(name)  # the pet variable is where the class object is instantiated
        print(pet.speak())
        print({pet})
        return pet


"""
Now with this PetShop factory, we can create a shop that sells either `cats` or `dogs`, and only initialize the shop
once. Then we reuse the same shop to define different cats or dogs that can be bought and made to bark from the shop.

This can be done as follows
"""

cat_shop = PetShop(Cat)
dog_shop = PetShop(Dog)

mycat1 = cat_shop.buy_pet('Tom')
mydog1 = dog_shop.buy_pet('Spike')

"""
In short, abstract factory methods can be used when we need to recreate many instances of the same object for our 
use cae. We use this design pattern when our code needs to create multiple instances of the same class, but we do not
want our object creation to depend on the main class itself. 
"""
