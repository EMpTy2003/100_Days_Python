#Treasure Map
r1=["😇","😇","😇"]
r2=["😇","😇","😇"]
r3=["😇","😇","😇"]
map=[r1,r2,r3]
print(f"{r1}\n{r2}\n{r3}\n")
position=input("Treasure location:")

horizontal=int(position[0])
vertical=int(position[1])

sel_row=map[vertical-1]
sel_row[horizontal-1] = "X"

print(f"{r1}\n{r2}\n{r3}\n")