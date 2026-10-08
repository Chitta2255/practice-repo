#it is a collection of Items
#lists are mutable/Change the value
#we create a list using []

marks = [98,97,96,90,'A',98.6]
print(marks,type(marks))

print(len(marks))#length

print(marks[-1])#Index Value

print(marks[0:3])#Slicing a list

print(marks[:2])

for points in marks:#using for loop
    print(points)

marks.append(75)#adding the value
print(marks)

marks.insert(4,75)#inserting the index value
print(marks)

print(97 in marks)#checks the value is existing or not

#marks.clear()
#print(marks,len(marks))

marks.remove("A")#removing a value
marks.remove(98.6)
print(marks)

Remove= marks.pop(4)#removing a value by index value
print(Remove)
print(marks)

marks.sort()#sorting the order
print(marks)

marks.reverse()#flips the order
print(marks)