# CMPT-120
# 10/18/18
# guessing game

def main():
    print ("PYTHON GUESSING GAME.")

main()

answer = "dog"

while True:
    print("I'm thinking of an animal")
    guess = input("What animal am I thinking of? ").lower()
    if guess.startswith("q"):
        break

    if guess == answer:
        print("You guessed correct!")
        yesOrNo = input("Do you like this animal? Enter 'yes' or 'no' ")
        if yesOrNo == "yes":
            print("Glad to hear!")
        if yesOrNo == "no":
            print("You should like this animal!")
        break
    elif guess != answer:
        print("Guess again!")
    
