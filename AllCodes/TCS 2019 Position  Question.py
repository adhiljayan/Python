x = int(input("Enter Number"))
xpos = 0
ypos = 0
looplinker=0
looper=1
for x in range(1,x+1):
    if looper > 4:
        looper = 1
        
        
    if looper == 1:
        looplinker +=10
        xpos += (looplinker)
        
    if looper == 2:
        looplinker += 10
        ypos += (looplinker)
        
    if looper == 3:
        looplinker += 10
        xpos = xpos - looplinker
        
    if looper == 4:
        looplinker += 10
        ypos = ypos - looplinker
    looper+=1
    
        
print(xpos , " " ,ypos)
