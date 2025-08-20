angle_a = int(input("enter the first no."))
angle_b = int(input("enter the first no."))
angle_c = int(input("enter the first no."))
angle_sum = angle_a + angle_b + angle_c
if angle_sum == 180 :
    if (angle_a ==  90 or angle_b == 90 or angle_c == 90):
        print(" right  angle triangle ")
    elif ( angle_a > 90 or angle_b > 90 or angle_c > 90 ):
        print(" obtuse angle triangle ")
    else :
        print(" acute angle triangle ")
else : 
    print("triangle angle  is not valid ")
