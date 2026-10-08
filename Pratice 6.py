#Write code to swap the values of two variables a = 5 and b = 10 without using a third variable
from enum import nonmember
from operator import and_
from platform import AndroidVer

a = 5
b = 10
a = a+b #15
b = a-b #15-10=5 b
a = a-b #15-5=10 a
print("a =",a)
print("b =",b)
#or using tuple
a = 5
b = 10
a , b = b, a # 5, 10 = 10 , 5 (a = 10 , b = 5)
print("a =",a)
print("b =",b)

#Write a program that takes two numbers as input from the user and prints their sum. (Hint: watch out for what input() returns.)
#a = int(input("Enter 1st number: "))
#b = int(input("Enter 2nd number: "))
#sum = a + b
#print("sum :",sum)

#Convert the float 9.99 to a string, then back to a float. Print the type at each step.

a = 9.99
print(type(a)) #float
a = str(a)
print(type(str(a))) #String
a = float(str(a))
print(type(a)) #float

#Write an expression using logical operators to check if a number is between 10 and 100 (inclusive).
number = 55
is_between = (10 <= number) and (number <= 100)
print(is_between)

#write a program using if,elif,else by taking input marks and giving him grade by his mark ?

marks = int ( input("Enter your marks: "))
if marks >= 90:
    print("A")
elif marks >=75:
    print("B")
elif marks >=50:
    print("C")
else:
    print("Fail")

#Write a nested if that checks: if a person is 18+ AND has a valid ID, print "Entry allowed"; if 18+ but no ID, print "ID required"; else print "Not allowed".

age = int(input("Enter Your Age: "))
has_id = input("Do you have an ID? (Yes/No): ") == "yes"
if age >= 18:
    if has_id:
        print("Entry Allowed")
    else:
        print("ID Required")
else:
        print("Entry Not Allowed")

#Write a for loop that prints all even numbers from 1 to 20 using range() with a step.

for i in range(2,21,2):
    print(i)

#Write a while loop that keeps asking the user to enter a number until they enter 0.

while True:
    num = int(input("Enter Your Number (0 to stop): "))
    if num == 0:
        break

#Given text = "Bangalore, India", write code to: (a) make it uppercase, (b) reverse it, (c) count how many times 'a' appears.

text = "Bangalore, India"
print(text.upper())
print(text [: : -1]) #Like Taking Range by Start ,Step, Stop
print(text.count('a'))

#Write a program using an f-string that takes a name and age as input and prints "Hi, my name is X and I am Y years old."

name = input("Enter Your Name: ")
age = int(input("Enter Your Age: "))
print(f"My name is {name} and I am {age} years old")

#Split the string "Java,Python,C++" into a list of languages using split().

languages = "Java,Python,C++"
print(languages.split(","))

#Create a list of 5 numbers. Write code to add a number, remove a number, sort it, and reverse it — printing the list after each step.

num = [10,22,55,2,1]
num.append(33)
print(num)
num.remove(2)
print(num)
num.sort()
print(num)
num.reverse()
print(num)

#Write code to remove duplicate values from [1, 2, 2, 3, 4, 4, 5] using a set.

num = [1,2,2,3,4,4,5]
unique_num = set(num)
print(unique_num)

#Create a dictionary representing yourself (name, age, skills as a list). Then: (a) print your name using get(), (b) add a new key city, (c) delete one key.

me = {"Name":"Prasad",
      "Age":28
    ,"Skill":["Python,Java,C++"]
      }
print(me.get("Name"))
me["city"]="Bangalore"
me.pop("Age")
print(me)

#Write a program that takes a sentence as input and counts how many vowels it contains.

sentences = input("Enter Your Sentences: ")
vowels = "aeiouAEIOU"
count = 0

for ch in sentences:
    if ch in vowels:
        count += 1
        print("Vowels Count: ",count)

#Write a program that takes a list of numbers and prints only the even numbers using a loop and if.

numbers = [1,2,3,4,5,6,7,8,9,10]
for n in numbers:
    if n%2 == 0:
        print(n)

#Given a dictionary of student names and marks, write code to find and print the student with the highest marks.

students = {"Ronaldo":86 , "Messi":83 ,"Mbappe":80}
topper_name = "none"
topper_marks = -1
for name,marks in students.items(): #this is using for loop and if Condition .
    if marks > topper_marks:
        topper_name = name
        topper_marks = marks
        print("Topper :", topper_name ,"With" , topper_marks , "marks")

        #OR in a Shorter way we can do this code with the help of max() .

students = {"Ronaldo":86 , "Messi":83 ,"Mbappe":80}
Topper = max(students , key=students.get)
print("Topper :",Topper , "With" , students[Topper] , "Marks")
