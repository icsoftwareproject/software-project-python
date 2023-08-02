# Python Data Types are Implemented as Classes 

All built-in data types in Python are implemented as classes

 ```
myString = 'abcde'
print(type(myString))
<class 'str'>
  ```
[Note] The str class gives us a number of methods we can call with strings, includeing myString.upper(), myString.lower(), myString.strip(), and so on. 

```
myList = [10, 20, 30, 40]
print(type(myList))
<class 'list'>
```

All lists are instances of the list class, which has many methods including myList.append(), myList.count(), myList.index(), and so on. 

When you write a class, you are defining a new data type. Your code provides the details by definint what data it maintains and what operations it can perform. 

After creating an instance of your class and assigning it to a variable, you can use the type() buil-in funciton to determine the class used to create it, just like with a built-in data type. 

```
oLightSwitch = LightSwitch()
print(type(oLightSwitch))
<class 'LightSwitch'>
```

## Definition of an Object

> Data, plus code that acts on that data, over time. 

A class defines what an object will look like when you instantiate one. An object is a set of instance variables and the code of the methods in the class from which the object was instantiated. 

Any number of objects can be instantiated from a class, and each has its own set of instance variables. When you call a method of an object, the method runs and uses the set of instance variables in that object. 