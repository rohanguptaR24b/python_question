num = int(input("enter the digit"))

total = 0
while (num >0):
    digit = num%10
    total += digit
    num = num//10
    
   

print(" sum of the digit:", total)