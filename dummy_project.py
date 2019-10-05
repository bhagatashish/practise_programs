a= '01234'
b = (0,1,2,3,4)
print(a[0:2])
print(b[0:2])
c = 'ah'
d='hello'
e= d.join(c)
print(e)

tup = ('red','orange','green')

new= [var for var in tup]
print(new)
new.remove('red')
new.append("green")
tup = tuple(new)
print(tup)

var= "helho world"

print(var.replace('h','j',2))


var1 = "my  name is nikhil"
list=[]
set= {""}

print(set)
j=0
for j in var1:
    for i in range(len(var1)):    
        if var[i] !=" ":
            s = var1[i]+ var1[i+1]
            print(s)
        else:
            break
    print(s)
        
    
            
   



    
        