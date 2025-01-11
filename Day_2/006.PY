#BMI CALCULATOR
height = (input("Enter your height in m: "))
weight = (input("Enter your weight in kg: "))
bmi = float(weight) / float(height) ** 2
new_bmi=int(bmi)
pri_bmi=str(new_bmi)
print("Your BMI Value is:" + pri_bmi)