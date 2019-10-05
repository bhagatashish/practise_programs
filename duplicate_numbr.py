data_list = [0, -23, 5, 0, 23, -6, 23, 67]
new_list = []
data_list1 = [0, -23, 5, 0, 23, -6, 23, 67]
data_list2 = [0, -23, 5, 0, 23, -6, 23, 67]
while data_list:
    minimum = data_list[0] #0
    for i in data_list:
        if i<minimum:
            minimum=i
    new_list.append(minimum)
    
    data_list.remove(minimum)
    print(data_list)
            
   
#bubble sort
n = len(data_list1)
for i in range (n):
    
    for j in range (0,n-i-1):
        
        if data_list1[j] > data_list1[j+1]:
            data_list1[j], data_list1[j+1]= data_list1[j+1],data_list1[j]
print(data_list1)
            
# order of n1:
count=0
for j in range (0,len(data_list2)-1):
    if data_list2[j]>data_list2[j+1]:
        data_list2[j], data_list2[j+1]= data_list2[j+1],data_list2[j]
    else:
        continue
    print(data_list2)
    
    
dic= {1:'hello','ggg':3 }


       

 



