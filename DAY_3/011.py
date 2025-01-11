print("Welcome to Treasure Island")
c1=input("Left L or Right R")
if c1== 'L':
    c2=input("Swim S or Wait W")
    if c2=='W':
        c3=input("Which Door? R or B or Y")
        if c3== 'B' or c3=='R':
            print("Game Over")
        else:
            print("You Won")
    else:
        print("Game Over")
else:
    print("Game Over")
