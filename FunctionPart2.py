#WAF to check if a number is odd or even

def CheckEvenOdd(num):
    if num % 2 == 0 :
        print(num , "is Prime")
    else:
        print(num , "is not Prime")

CheckEvenOdd(22)
CheckEvenOdd(55)

#WAF to count the number of vowels in a string

def CountVowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
            print("Vowels Count: " , count)

CountVowels("MotherFucking millionaire")

#WAF to print if a number is prime or not

def CheckPrime(num):
    isPrime = True
    for i in range (2 , num):
        if num % i == 0:
            isPrime = False
            break
    if isPrime:
        print(num ,"is Prime")
    else:
        print(num ,"is Not Prime")


CheckPrime(7)
CheckPrime(8)

#WAF to return the average marks if a list of marks is passed as parameter

def AverageMark(Marklist):
    total = sum(Marklist)
    avg = total/len(Marklist)
    return avg

result = AverageMark([90,91,85])
print("Average is ",result)