def dis_num(num):
    n=len(num)
    total=0
    num1=int(num)
    for pos in range(n):
        digit = int(num[pos])
        position = pos+1
        total += digit ** position
    return total == num1
a=input("Enter the number")
valid=dis_num(a)
if valid==True:
    print("The number is a Disarium number")
else:
    print("The number is not a Disarium number")
