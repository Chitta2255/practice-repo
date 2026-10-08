text = "Hello Savage"
print(text.replace("Hello","Hi")) #replace old value to new

text = "Iphone 17 pro,Macbook Air M1,Kia Sonet"
print(text.split(" , ")) #Split makes it list

text = "  hello  "
print(text.strip()) #eliminates extra whitespaces

text = "Hello world"
print(text.find("world")) #Find the text by Index value

text = "Bananana"
print(text.count('a')) #count the appearance of a

name ="Savage"
age = 26
print(f"My name is {name} and I am {age} years old. ") #using f string it is easy to insert variable into text