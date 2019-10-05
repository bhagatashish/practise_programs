a= 10
b=a
print(id(a),id(b)) # it will have same memory allocation and value
print("a and b is " + str(id(a)==id(b)))

b=12
print(id(a),id(b)) # it will different memory allocation and value
print("a and b is " + str(id(a)==id(b)))
b=10
c=10

print(id(a),id(b),id(c)) # it will have same memory allocation and value
print("a and b is " + str(id(a)==id(b)))

list= [1,2,3]
list1=list
print(id(list),id(list1)) # it will have same memory allocation and value
list1.append(4)
print(id(list),id(list1)) # it will have same memory allocation and value even if we change the value in list1, the orginal list will also get changed\
print(list,list1)
print(help(int))