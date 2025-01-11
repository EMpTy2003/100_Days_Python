#Adding Even Numbers
total=0
for num in range(0,101,2):
    total+=num
print(total)

#Method 2
total2=0
for num in range(0,101):
    if num%2==0:
        total2+=num
print(total2)