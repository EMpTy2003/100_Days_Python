#Multiple if statements in succession
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill=0
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age<12:
        bill=5
        print("Child tickets are $5.")
    elif age == 12 or age <=18:
        bill=7
        print("Youth tickets are $7.")
    else:
        bill=12
        print("Adult tickets are $12.")
        
    photo=input("Need Photos? Y or N")
    if photo == 'y' or photo == 'Y':
        bill+=3
        print(f"Total is {bill}")
    elif photo == 'N' or photo=='n':
        print(f"Total is {bill}")
    else:
        print("Invalid Choice")
else:
    print("Sorry, you have to grow taller before you can ride.")