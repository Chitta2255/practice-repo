#part1 print all the odd number in range of 1 to 20
for i in range(1,21):
    if i%2!=0:
        print(i)

#part2 print table 57
for i in range(1,11):
    print(57 , "x" , i , "=" , 57 * i)

#part3 multiple of 3 [1 to 50]=> 15 skip
for i in range(1,51):
    if i == 15:
        continue
    if i % 3 == 0:
       print(i)

#part4 take two integers a and b as input.
#find and print the first number between 1 to 1000 that is divisible by both
a = int(input("Enter a :"))
b = int(input("Enter b :"))
for i in range (1,1001):
    if i % a == 0 and i % b == 0:
        print("First common Multiple :" ,i)
        break