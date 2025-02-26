#Calculator Part - 1 - Combining Dictionaries and Functions

def add(n1, n2):
    return n1+n2

def sub(n1, n2):
    return n1-n2

def multi(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {"+":add, 
           "-":sub,
           "*":multi,
           "/":divide
           }

num1=int(input("What's the first number?: "))
num2=int(input("What's the second number?: "))

for symbol in operations:
    print(symbol)
    
operation_symbol=input("Pick an operation from the above: ")
calculation_function=operations[operation_symbol]
first_answer = calculation_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {first_answer}")

operation_symbol=input("Pick an operation from the above: ")
num3=int(input("What's the next number?: "))
calculation_function=operations[operation_symbol]
second_answer = calculation_function(calculation_function(num1, num2), num3)

print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")