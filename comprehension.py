'''
There are 4 types of comprehensions
a. List comprehension
b. Dic comprehension
c. Set comprehension 
d. Generator comprehension 
'''
#if the user want to make a new list using old list , he has to use below code 
a =[1,2,3,4,5,6]
b=[]

for i in a:
    b.append(i)
    
print("the new list would be "+ str(b))
# but we can simply the task by using list comprehension 

new_list = [i for i in a ]
print('the new list is ' + str(new_list))

#we want to create an output dictionary which contains only the odd numbers that are present in the input list as keys and their cubes as values. 
list=[1,2,3,4,5,6,7,8,9]

dic= {var:var*3 for var in list if var%2!=0}
print(dic)
#Set comprehension : Set comprehension is similar to list , but they start with {} and remove duplicate values
list=[1,2,3,4,5,1,1,3,4,4,5,5,1]
set_number= {var for var in list}
print(set_number)

# generator comprehension : these are similiar to list but list use [] and generator comprehension use () , the only difference is gene
list=[1,2,3,4,5,1,1,3,4,4,5,5,1]
generator_comp= (var for var in list)
print(generator_comp)
var = [i for i in generator_comp]
print(var)

