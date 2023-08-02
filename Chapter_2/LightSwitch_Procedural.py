# Procedural light switch

def turnOn():
    global switchIsOn
    # turn the light on 
    switchIsOn = True

def turnOff():
    global switchIsOn
    # turn the light off
    switchIsOn = False
    
# Main code
switchIsOn = False     # a global Boolean variable

# Test code
print(switchIsOn)
turnOn()
print(switchIsOn)
turnOff()
print(switchIsOn)
turnOn()
print(switchIsOn)

# Because we've used a global variable to represent the state (in this case, the variable switchIsOn)
# this code will only work for a single light switch, but one of the main goals of writing function 
# is to make reusable code. 