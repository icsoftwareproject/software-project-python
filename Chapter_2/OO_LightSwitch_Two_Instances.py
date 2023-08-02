# OO_LightSwitch

# [Note] One of the key features of OOP is that you can instantiate as many objects 
# as you want from a single class, in the same way that you can make endless 
# cake from a Bundt cake pan. 

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
    
#[Note] The improtant point here is that each object that you create from a class 
# maintains its own version of the data. In this case, oLightSwitch1 and oLightSwitch2 each have 
# their own instance variable, self.switchIsOn. 

#[Note] Any changes you make to the data of one object will no affect the data of another object. 
# You can call any of the methods in the class with either object.  

oLightSwitch1 = LightSwitch()  # create a LightSwitch object
oLightSwitch2 = LightSwitch()  # create another LightSwitch object

#  Test code
oLightSwitch1.show()
oLightSwitch2.show()
oLightSwitch1.turnOn() # Turn switch 1 on
# Switch 2 should be off at start, but this makes it clearer
oLightSwitch2.turnOff()  
oLightSwitch1.show()
oLightSwitch2.show()

# Each object created from a class gets its own set of instances variables, 
# independent of any other objects instantiated from that class. 
# In the case of the LightSwitch class, there is only one instance variable, 
# self.switchIsOn, so have multiple LightSwitch objects, each with its own 
# independent value of True or False for its self.switchIsOn variable. 