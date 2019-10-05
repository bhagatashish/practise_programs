from msilib.schema import RemoveRegistry

list1=list()
count=10
import pytest

class pattern():
    def remove_duplicates(self):
        list=[28, 42, 28, 16, 90, 42, 42, 28,2,3,2]
        list2= []
        for i in list:
            if i not in list2:                
                list2.append(i)
        list2.sort()
        print(list2)
    def oneside(self):
        num= list()
        self.k=10
        for i in range(0,10):
            print("*" * i)
    def inverse(self):
        for j in range(0,10):
            
            print("*" * self.k)
            self.k=self.k-1                          
           
               
    def print_numbers(self):
        num= int(input("input the number"))
        for i in range(1,num+1):
            for j in range(1,i+1):
                print(j,end='')
            print()
            
    def heart_shape(self):
        for row in range(6):
            for col in range(7):
                if (row==0 and col%3!=0) or (row==1 and col%3==0) or (row+col==8) or (row-col==2):
                    print("*",end='')
                
                else:
                    print(" ",end='')
            print("")
    
    def Triangle(self):
        for row in range(0,6):            
            for col in range(0,6-row-1):
                print(" ",end='')
            for col in range(0,row+1):
                print("x",end=' ')                
            
            print('')
                
                
                
    def method1(self):
        return(self.remove_duplicates(),self.heart_shape(),self.Triangle(),self.oneside(),self.inverse(),self.print_numbers())           
       
pattern().method1()

    
