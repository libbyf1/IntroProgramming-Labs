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
    if guess == answer:
        print("You guessed correct!")
        break
    else:
        print("Guess again!")
