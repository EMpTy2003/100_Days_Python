#Leap Year or Not
y=2024
if y%4==0:
    if y%100==0:
        if y%400==0:
            print("This is a leap year.")
        else:
            print("This is not a leap year.")
    else:
        print("This is a leap year.")
else:
    print("This is not a leap year.")