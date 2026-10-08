#Class is a User defined Blueprint or Prototype.
#Self keyword is mandatory for calling variable name into method.
#Constructor name should be __init__.
#Constructor is one method which is automatically called when you create object for any Class.

class Calculator:
    num = 100 #class Variable

    def __init__(self, a , b): #Default Constructor / Parameterised Constructor.
        self.Firstnumber = a #Instance Variable
        self.Secondnumber = b #Instance variable
        print("I am called automatically when Object is created")

    def Getdata(self): #class method
        print("I am now executing as Method in class Calculator")

    def Summation(self):
        return self.Firstnumber + self.Secondnumber + Calculator.num #for calling class variable we have to use class
    #name. variable or self.varible name

obj = Calculator(2, 3) #Syntax for Object creation
obj.Getdata() #calling Method
print(obj.Summation())

obj = Calculator(4, 5) #Arguments
obj.Getdata()
print(obj.Summation())