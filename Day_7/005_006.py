#Hangman Step 2

import random
word_list=["camel", "baboon", "awkward"]
chosen=random.choice(word_list)


print(f"psst, the solution is {chosen}")




display=[]
length=len(chosen)
for _ in range(0,length):
    display+="_"
print (display)

guess=input("Guess a Letter: ").lower()




for position in range(length):
    letter=chosen[position]
    if letter == guess:
        display[position]=letter
        
        
        
print(display)