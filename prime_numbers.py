'''
Created on Jul 2, 2019

@author: AH0128901
'''
#:Java Program to Find the Largest Two Numbers in a Given Array
list = [12,23,1,2,8,40,55]

largest_num = list[0]
# first way to get largest num
for num in list:
    if num > largest_num:
        largest_num = num
print(largest_num)

# using python built in function
print(f"the larget number is {max(list)}")

# for 2nd largest num
list.sort()
print(f"the 2nd largest num is {list[-2]}")






    