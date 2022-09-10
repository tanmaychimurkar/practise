""" Inheretence
"""

"""
Classes that inheret from other classes also get the methods of the class from which they are inheriting. This is 
shown in the example below.
"""


class Robot:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print(f'Hey there, {self.name}')


class SuperiorRobot(Robot):
    pass


r = SuperiorRobot('Ross')
r.say_hi()

"""
When inheriting class and checking their type, always use isinstance() method instead of the type method. type only 
returns true if the instance if the exact type of the class that defined it, but isinstance can follow the chain of 
class inheritance while checking the type of the instance. 
"""

"""
Sometimes when we do method overriding for an method defined in the parent class, we often might want to use some parts
of the method from the parent class in our subclass. For this, we can invoke the method from the parent class into our
subclass as follows
"""


class RobotOverrideHi(Robot):
    def say_hi(self):
        Robot.say_hi(self) # here we could also change the Robot to super() and it would be the same
        print(f'Well, that was good {self.name}')


ovr = RobotOverrideHi('Rachel')
ovr.say_hi()

###############################################################################################################

"""
Multiple inheritance: So far we have seen how single inheritance works. Now we take a look at multiple inheritance. 
"""