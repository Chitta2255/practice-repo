#Smart AI ChatBot
import datetime
import time



name =input("Enter Your Name:")
presentHour = datetime.datetime.now().hour
if 4<= presentHour <= 12:
    print("Good Morning!",name)
elif 12<= presentHour <= 17:
    print("Good Afternoon!",name)
elif 17<= presentHour <= 20:
    print("Good Evening!",name)
else:
    print("Good Night!",name)

responses = {"hello":"hi,welcome how can i help you!",
             "how are you":"i am very fine ,thank you.",
             "who are you":"i am smart ai chat bot.",
             "motivate me":"Keep going every bug of your project make you a better developer.",
             "happy":"great to hear that.",
             "what is function":"i dont know yet , but i will learn soon."}

def getResponse(Userquestion):
    Userquestion = Userquestion.lower()
    for eachkey in responses:
        if eachkey in Userquestion:
            return responses[eachkey]
    return "I am not capable of this thing to do."

while True:
    userInput = input("Enter Your Question:")
    reply = getResponse(userInput)
    print("Got Response:",reply)

    if "bye" in userInput.lower():
        break