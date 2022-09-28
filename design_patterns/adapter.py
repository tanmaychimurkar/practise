""" Adapter Design
"""

"""
This design allows object with incompatible interface to interact with each other. 

We wrap the incompatible object with a adapter and all the conversion between the interfaces takes place behind the 
scenes. 

We have two types of adapters: Object adapters and class adapters.

Object adapter acts as a wrapper, while the class adapter inherits from both the client and the legacy code.

The adapter kinda acts like a middleware between the two classes in consideration. 
"""

"""
The first example shows how we can create an adapter that acts as a bridge between the two incompatible classes. 
However, cases like these never arise in normal application code, so this example is not the best to learn adapters
"""


class Cat:
    def meow(self):
        return f'I can say meow'


class ModernCat:
    def modern_meow(self):
        return f'!!!rehtaf ruoy ma I ,ekuL'


class AdapterInherited(Cat, ModernCat):

    def meow(self):
        return f'{self.modern_meow()[::-1]}'


class AdapterObject(ModernCat):

    def __init__(self, old_class):
        self.old_class = old_class

    def meow(self):
        return f'{self.old_class.modern_meow()[::-1]}'


def bridge_to_interact(adapter):
    print(adapter.meow())


### usage and calls ###

original_cat = Cat()
bridge_to_interact(original_cat)  # we use the bridge to interact since that is the only function we have access to

modern_cat = ModernCat()
# bridge_to_interact(modern_cat)
# we want our new modern method to also be able to work with the meow function, but the above function will break for
# obvious reasons

adapter = AdapterObject(modern_cat)
bridge_to_interact(adapter)

# we could also assign the AdapterInherited class to adapter and the same functionality will be returned.

"""
We saw above the case when the code does not have to take any inputs. However, since that is hardly the case, we now see
how we can create an adapter that takes arguments in the classes as well.
"""


class OldCat:

    def __init__(self, name):
        self.name = name

    def say_meow(self, name):
        return f'Meow, I am {name}'


class CyberCat:

    def __init__(self, name):
        self.name = name

    def modern_meow(self, name):
        return f'Luke, I am {name}, meow, your father'


class Adapter:

    def __init__(self, new_interface, func):
        self.new_interface = new_interface
        self.__dict__.update(func)

    def __getattr__(self, item):
        return getattr(self.new_interface, item)

    def original_dict(self):
        return self.new_interface.__dict__


all_objects = []
old_cat = OldCat('Tom')
all_objects.append(Adapter(old_cat, make_noise=old_cat.say_meow))