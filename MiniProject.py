#Calculator
num1=int(input("Enter Your First Number: "))
num2=int(input("Enter Your Second Number: "))
OP=input("Enter Your Operator (+,-,*,/,%,**) :")
if OP == "+":
    print(num1+num2)
elif OP == "-":
    print(num1-num2)
elif OP == "*":
    print(num1*num2)
elif OP == "/":
    print(num1/num2)
elif OP == "%":
    print(num1%num2)
elif OP =="**":
    print(num1**num2)
else:
    print("INVALID OPERATION")
