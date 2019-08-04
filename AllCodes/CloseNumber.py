#PF-Prac-13
def close_number(num1,num2,num3):
    flag=False
    flag = abs(num1-num2) == 1 and abs(num1-num3) >= 2 and abs(num2-num3) >= 2   
    flag = flag or abs(num2-num3) == 1 and abs(num2-num1) >= 2 and abs(num1-num3) >= 2
    flag = flag or abs(num1-num3) == 1 and abs(num1-num2) >= 2 and abs(num3-num2) >= 2
    return flag
print(close_number(6,6,9))