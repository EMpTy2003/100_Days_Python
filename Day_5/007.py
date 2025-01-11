#fizz buzz
#if number is divisible by 3 fizz, if divisible by 5 buzz
total=0
for num in range(1,101):
    total=num
    if total % 5 == 0 and total % 3 == 0:
        print("FizzBuzz")
    elif total % 5 == 0:
        print("Buzz")
    elif total % 3 == 0:
        print("Fizz")
    else:
        print(total)