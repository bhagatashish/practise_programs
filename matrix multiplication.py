a = [[6 , 7 , 9],
     [3 , 4 , 1],
     [5,  2 , 8]]

b = [[6,  7 , 9],
     [3 , 4 , 1],
     [5 , 2 , 8]]



for i in range(0,len(a)):
     for j in range(0,len(a)):
          print(a[i][j] * b[j][i])
print(a)
print("deemo")