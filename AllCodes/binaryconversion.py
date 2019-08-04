x = int(input("Enter Number"))
str1=""
str2=""
while(x!=0):   
    str1 = str1 + str(x%2)
    x=x//2
    
for i in str1:
    str2= i + str2
    
print(str2)
