
num = 1234
list=[]
j=0
num = [int(x) for x in str(num)]
print(num)
square=[num1*num1 for num1 in range(1,len(num)+1) ]
print(square)
for i in range(len(num)):
    num1=num[j]*num[j]
    j=j+1
    print(num1)
