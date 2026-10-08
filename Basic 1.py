print("Hello Python World", "Chitta ")

My_name = "My Name is Savage"
age = 26
height = 6.0
text = "Wass up"
number = 2255

print (My_name)
print(age)
print(height)
print(text)
print(number)

print(type(text))
print(type(number))
print(type(My_name))
print(type(age))
print(type(height))

#type_Conversion
age_text = "26" #String To Integer
age_number = int (age_text)
print (age_number + 10)
#OR
number = 10 #Integer to String
number_text = str(number)
print (number_text)
#Math_Operator
a = 56
b = 65
print (a + b)
print (a - b)
print (a * b)
print (a / b)
print (a // b)
print (a % b)
print (a ** b)
#String-Concatenation
name = "Savage"
greeting = "hello," + name + "!"
print(greeting)
num_plate = 2255
print("Hello " + name + " Your Number Plate is " + str(num_plate))
num = 26
message = f"{name} is {num} years old." #F-string is used for
print(message)

print(len(name))
print(name.upper())
print(name.lower())
print(name[0])
print(name[-1])
print(name[1:3])
#Getting_Input_From_User
name = input ("What is your name : ")
print(f"Wass up , {name}")
age = input("whats your age : ")
age = int(age)
print(f"Next year you will be {age + 1}. ")
#Making_Decision(If,Elif,Else)
#==   # equal to
#!=   # not equal to
#>    # greater than
#<    # less than
#>=   # greater than or equal to
#<=   # less than or equal to
age = 26
if age >=18:
    print("You are an Adult")
elif age >=15:
    print("You are a teen")
else:
    print("You are a Kid")

#Combining Condition
Number = 20
has_id=True
if Number>= 20 and has_id:
    print("You may enter")
    if age<20 and not has_id:
        print("You may not enter")

        #For Loop Range()
    #range(start,stop,step)
    for i in range (1,11):
        print(i)