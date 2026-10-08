#Function is a group of related statements that performs a specific task.
#Function Declaration.

def Greetme(name):
    print("Good Morning "+ name)

def AddInteger(a,b):
    return(a+b)

Greetme("Savage")    #Function call
print(AddInteger(1111,1144))

def cal_gst(price):
    new_price = price + price * 0.18
    return new_price

print(cal_gst(2255))

def Addall(*numbers):
    total = 0
    for n in numbers:
        total += n
        return n