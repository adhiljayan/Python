x = input("Enter String")
even=""
odd=""
for y in range(0,len(x),2):
    even += x[y]
    if y+1 < len(x):
        odd += x[y+1]

print(even+odd)
    