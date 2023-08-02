# In procedural programming: global scope and local scope 

# In object-oriented programming, we have: object scope (also known as,  class scope or instance scope)
# [Class scope definition] the scope consists of all the code inside the class definition 

# [Methods variables] methods can have both local variables and instance variables 

# [Local variables] Any variable whose name does not start with "self." is a local variable 
# and will go away when that method exists, meaning other methods within the class can no 
# longer use that variable 

# [Instance variables] In a method, any variable whose name begins, by convetion, 
# with the prefix "self." (for example, self.x). Instance variables have object (class) scope, 
# which means they are available to all methods defined in a class. 

class MyClass():

    def __init__(self):
        self.count = 0

    def increment(self):
        self.count = self.count + 1  