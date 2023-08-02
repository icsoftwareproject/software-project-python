# OO_LightSwitch

#[Example] Give an example of On-demand cake-baking business 

#[Class Intuition] You can think of a class as a template that defines what an 
# object will look like when one is created. We create objects from a class. 

# [CLass Definition] Code that defines what an object will remember (its data or state) and
# the things that it will be able to do (its functions or behavior). 

#[Note] The first method in every class should have the special name __init__ 

#[Note] In reality, the __init__() method is not stricly required. 
# However, it's generally considered good practice to include it and use it for initialization. 

class LightSwitch():
    def __init__(self):
        self.switchIsOn = False

    def turnOn(self):
        # turn the switch on 
         self.switchIsOn = True

    def turnOff(self):
        # turn the switch off
         self.switchIsOn = False

    def show(self):  # added for testing
        print(self.switchIsOn)

#[Observation] Notice that this code defines a single variable, self.switchIsOn, 
# which is initialized in one function, and contains two other function for the behaviors: 
# turnOn() and turnOff()


#[Instantiation] The process of creating an object from a class
#[Instiantion Example] creating a LightSwitch object 

oLightSwitch = LightSwitch()  # create a LightSwitch object

#[Note] when you instantiate an object from a class, Python takes care of constructing the 
# the obejct (allocating memory) for you. The special __init__() method is called the 
# "initializer" method, where you give variables initial values. 

#[Method] OOP functions are given a special name: method 
#[Method definition] A function defined inside a class. A method always has at least one parameter, 
# which is usually named self. 

#  Calls to methods
oLightSwitch.show() # call the show method of oLightSwitch
oLightSwitch.turnOn() # call the turnOn method of oLightSwitch
oLightSwitch.show()
oLightSwitch.turnOff() # call the turnOff method of oLightSwitch
oLightSwitch.show()
oLightSwitch.turnOn() # call the turnOn method of oLightSwitch
oLightSwitch.show()
