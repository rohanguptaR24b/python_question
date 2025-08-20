a = int(input(" enter a number"))
b = int(input(" enter the power value"))

result = 1 
i = 1 
while i <= b :
    result *= a 
    i += 1 
print (a , "^", b , "= " , result)