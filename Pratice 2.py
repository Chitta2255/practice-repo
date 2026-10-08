product1 = float(input("enter product 1 price: "))
product2 = float(input("enter product 2 price: "))
product3 = float(input("enter product 3 price: "))
total_value = product1 + product2 + product3
avg_value= total_value / 3
print("Total Value: ",total_value)
print("Average Value: ",avg_value)

name = input("Enter Your SuperHero Name: ")
first_letter = name[0]
print(first_letter == 'S' or first_letter == 's')

# in OR operator one expression should be true
#in AND operator both expression should be true
#NOT operator does the opposite of the expression given
#Indentation means giving Proper Gaps/Spaces
marks = 85
if marks >=80:
    print("You can drive/vote")
elif marks <80 and marks <=70 :
    print("You can drive/vote")
else:
    print("You Cant Drive/Vote")