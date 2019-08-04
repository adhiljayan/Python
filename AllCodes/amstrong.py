x = input("EnterNumberto Check Amstrong Number")
sum=0
for y in str(x):
    sum += int(y) * int(y) * int(y)

if sum == int(x):
    print("Amstrong Number")
else:
    print("Not")