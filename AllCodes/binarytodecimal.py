x = input("Enter Binary Number")
x=x[::-1] # Reversed
sums=0
sum1=1

for k in range(0,len(x)):
    if x[k] == str(1):
        sums += sum1    
    sum1 += sum1
print("Number is ",sums)

# Code Link in Description
# Lets Check











#Another Way
'''
x = input("Enter Binary Number")
str1=""
sums=0
loopcounter=0

#x=x[::-1]
for i in x: #Reversal of Given Binary Number
    str1 = i + str1

sum1=1
for k in x:
    if str1[loopcounter] == str(1):
        sums += sum1
    loopcounter +=1
    sum1 += sum1
    

print(sums)

'''

