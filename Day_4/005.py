#Banker roulette
import random
name_st=input("Enter with ,: ")
names=name_st.split(", ")
x=len(names)
choice=random.randint(0,x-1)
print(choice)
print(names[choice], "Pays the bill")