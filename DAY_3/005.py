#BMI CALCULATOR
height = (input("Enter your height in m: "))
weight = (input("Enter your weight in kg: "))
new_bmi = float(weight) / float(height) ** 2
print (new_bmi)
if new_bmi<18.5:
    print("You are underweight.")
elif new_bmi > 18.5 and new_bmi<25:
    print("You have a normal weight.")
elif new_bmi > 25 and new_bmi<30:
    print("You are overweight.")
elif new_bmi > 30 and new_bmi<35:
    print("You are obese")
else:
    print("You are clinically obese.")