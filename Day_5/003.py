#Average Height
height=input("List of heights").split()
for n in range(0,len(height)):
    height[n]=int(height[n])
print(height)

total=0
for h in height:
    total+=h
print(total)

count=0
for avg in height:
    count+=1
print(count)

average=total/count
print ("Average height is", int(average))
