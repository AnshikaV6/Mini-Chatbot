import datetime


print("Namaste! Welcome to Gluco AI Chatbot")
print("You can ask me basic question~~ ",
      "Type 'bye' to exit from the bot",end="\n")


presenthour=datetime.datetime.now().hour
name=input("Enter your name:")
if 5<= presenthour <=11:
    print(f"Good Morning {name}")
elif 11< presenthour <= 16:
    print(f"Good Afternoon {name}")
elif 16< presenthour <=18:
    print(f"Good Evening {name}")
else:
    print(f"Good Night {name}")


#chatbot memory
responses={
    "hello":"Hi,Welcome!  How can I help you?",
    "how are you":"I am good! What about you?",
    "who are you":"I am a Smart AI Chatbot made by Anshika ",
    "motivate me":"Sure,Keep going! because Every small effort of yours can make a huge change if repeated again and again",
    "happy":"Great to hear that ",
    "what is python":"python is a programming language that is very popular in coding world ",
    "tell me your functions":"I can motivate you,I can tell you about python ",

}
#take user input


def getResponseOfBot(userQuestion):
    userQuestion=userQuestion.lower()
    for eachkey in responses:
        if eachkey in userQuestion:
            return responses[eachkey]

    return "I am not able to tell that yet. I am still in learning mode"


while True:
    userinput=input("Please ask your question:")
    reply=getResponseOfBot(userinput)
    print(reply)
    if userinput.lower()== "bye":
        print("Thanks for talking to me")
        break
