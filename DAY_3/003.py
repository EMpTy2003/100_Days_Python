#Odd or Even Introducing the Modulo
#The modulo is the percentage sign % and it is used to find the remainder of a division sum.
#For example, 6 divided by 2 is 3 with no remainder, so 6 % 2 is 0.
#7 divided by 3 is 2 with a remainder of 1, so 7 % 3 is 1.
#The modulo is useful for finding out if a number is odd or even.
#If a number is divided by 2 and has a remainder of 0, it is even.
#If a number is divided by 2 and has a remainder of 1, it is odd.
#We can use this to make a simple program that checks if a number is odd or even.
#We can also use the modulo to check if a number is a multiple of another number.
#For example, 10 % 5 is 0, so 10 is a multiple of 5.
#The modulo is a very useful operator and is used in many programs.
#Let's make a simple program that checks if a number is odd or even.
#Type the following code into your file:

n=int(input("Enter a number: "))
if n%2==0:
    print("This is an even number.")
else:
    print("This is an odd number.")
    