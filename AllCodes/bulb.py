#Both Bulbs and Members
x = int(input("Enter Total Number Of Bulbs"))
xx = int(input("Enter Total Number of Members"))


onoff=[0 for i in range(0,x)]
y=1
for k in range(1,xx+1):
    for z in range(y,x+1,y):
        if onoff[z-1] == 1:
            onoff[z-1]=0
        else:
            onoff[z-1]=1
    y +=1
y=0    
for g in onoff:
    if g==1:
        y+=1
print ("Total Bulbs On : ",y)




#Only For Pulbs Not Members
''' 
x = int(input("Enter Total Number Of Bulbs"))
onoff=[0 for i in range(0,x)]
y=1
for k in range(1,x+1):
    for z in range(y,x+1,y):        
        if onoff[z-1] == 1:
            onoff[z-1]=0
        else:
            onoff[z-1]=1
    y +=1
y=0    
for g in onoff:
    if g==1:
        y+=1
print ("Total Bulbs On : ",y)
'''