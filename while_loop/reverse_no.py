n  = int(input("enter the digit"))
a = 0
while (n>0):
    num = n%10
    a = a*10+num
    n = n//10
print(a)