'''
Created on Jul 2, 2019

@author: AH0128901
'''
#:Java Program to Find the Largest Two Numbers in a Given Array
list = [12,23,1,2,8,40,55]
list.sort()
print(list)
len = len(list)-1
print (list[len])
print(list[len-1])
for i in range (len(list)):
    print(list[i])
    