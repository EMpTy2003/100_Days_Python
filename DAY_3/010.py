#Love Calculator
print("Welcome to love Calculator")
him=input("Your Name: \n")
her=input("Their Name: \n")

comb= him + her
lower=comb.lower()
t=lower.count('t')
r=lower.count('r')
u=lower.count('u')
e=lower.count('e')
l=lower.count('l')
o=lower.count('o')
v=lower.count('v')
f=lower.count('e')
true=t+r+u+e
love=l+o+v+f
score=int(str(true) + str(love))

print (score)

if (score < 10) or (score > 90):
    print(f"Score is {score}, coke and mentos")
elif score >=40 and score <= 50:
    print(f"Score is {score}, alright")
else:
    print(f"score is {score}")