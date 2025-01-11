import math
def paint_calc(height, width, cover):
    area= height*width
    paint=math.ceil(area/coverage)
    print(f"Area: {area}")
    print(f"You'll need {paint}")

#Paint Area Calculator
test_h = int(input("Height of the wall: "))
test_w = int(input("Width of the wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w,cover=coverage) 

