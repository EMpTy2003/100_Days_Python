#Pizza Order Practice
print("Welcome")
size=input("S, M or L:  ")
add_pep=input("Pepperoni? Y or N:  ")
xcheese=input("Extra Cheese? Y or N:  ")
bill=0
if size == 's' or size=='S':
    bill=15
elif size == 'm' or size=='M':
    bill=20
elif size == 'l' or size=='L':
    bill=25
else:
    print("Invalid Choice")
if add_pep=='Y' or add_pep=='y':
    if size == 's' or size=='S':
        bill+=2
    else:
        bill+=3
if xcheese=='Y' or xcheese=='y':
    bill+=1
print(bill)