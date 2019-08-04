twomatrix=[]
matrix = [['1', '2', '3','4','5'],
          ['6', '7', '8','9','10'],
          ['11', '12', '13','14','15'],
          ['16', '17', '18','19','20'],
          ['21', '22', '23','24','25']]

colcounter = 0
rowcounter = 0
counter=0
for row in matrix:    
    for col in row:
        try:
            if matrix[rowcounter][colcounter+1].isdigit() == True and matrix[rowcounter+1][colcounter].isdigit()== True:
                counter+=1 #NotUsed
                #str=matrix[rowcounter][colcounter] + "," + matrix[rowcounter][colcounter+1]+ "," + matirx[rowounter+1][colcounter] + "," + matrix[rowcounter+1][colcounter+1]
                str=matrix[rowcounter][colcounter] + "," + matrix[rowcounter][colcounter+1] + "," + matrix[rowcounter+1][colcounter] + "," + matrix[rowcounter+1][colcounter+1]
                twomatrix.append(str)                                 
        except:
            pass
        colcounter += 1
    rowcounter+=1
    colcounter = 0
    
print("Total Counter " , counter)
tempmatrix=[]
localharsedcounter=0
tempcounter=0
print("Two matrix")
print(twomatrix)
print("----------------------------------------")
for x in twomatrix:
    tempmatrix.clear()
    tempmatrix.append(x.split(","))
    for y in tempmatrix:
        if tempcounter < len(y):            
            if len(y[tempcounter]) == 1:
                #print(tempmatrix)
                continue
            else:
                print( y[tempcounter])
                    #print(y[te])
        tempcounter +=1
        
        
        