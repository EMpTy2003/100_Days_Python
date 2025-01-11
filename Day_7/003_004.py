#Hangman Start Step 1
#Pic
import random
word_list=["camel", "baboon", "awkward"]
chosen=random.choice(word_list)
guess=input("Guess a Letter: ").lower()
for letter in chosen:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")