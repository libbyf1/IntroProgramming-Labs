
def promptForWords():
    'global noun, verb, adjective, place'
promptForWords()

def makeAndPrintSentence():
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    adjective = input("Enter an adjective: ")
    place = input("Enter a place: ")
    print("Take your " + adjective + " " + noun + " and " + verb + " to the " + place + "!")
makeAndPrintSentence()

def main(promptForWords, makeAndPrintSentence):
    return promptForWords + makeAndPrintSentence


