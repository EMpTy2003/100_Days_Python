import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


art = [rock, paper, scissors]
choice = ["rock", "paper", "scissors"]


user = int(input("Choose: Rock (0), Paper (1), or Scissors (2): "))

if user not in [0, 1, 2]:
    print("Invalid input. Please choose 0, 1, or 2.")
else:
    
    comp = random.randint(0, 2)

    # Display the choices
    print(f"\nYou chose:\n{art[user]}")
    print(f"Computer chose:\n{art[comp]}")

    # Determine the winner
    if user == comp:
        print("It's a draw!")
    elif (user == 0 and comp == 2) or (user == 1 and comp == 0) or (user == 2 and comp == 1):
        print("You win!")
    else:
        print("You lose!")
