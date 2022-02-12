import random


print("Hello World")

def GuessVal():
    inputstr=input("What is your guess?")
    while True:
        try:
            Guess=int(inputstr)
            break
        except ValueError:
            print("That ain't a number doofus!") 
            Guess=-1
            break
    return Guess


Answer=random.randint(0.0,100)
Guess=GuessVal()
while Answer!=Guess:
    if Answer>Guess :
        print("Answer is larger than Guess")
    if Answer<Guess :
        print("Answer is smaller than Guess")
    Guess=GuessVal()
print("Guess is correct")

