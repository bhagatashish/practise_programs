class fibonacci_series:
    def series1(self):
        num = list()
        num1=list()
        num2=list()
        for i  in range(10):
            num.append(i)        
        print(num)
        
        j=1
        
        for i in range(len(num)-1):
            
            new_num=num[i]+num[j]
            j= j+1
            print(new_num)
            num1.append(new_num)
        print(num1)
        #another way
        n1=0
        n2=1
        count=0
        
        while count<=len(num):
            
            nth = n1+n2
            
            n1=n2
            n2=nth
            count=count+1
            
        print(num2)
    
    def series2(self):
        return self.series1() # there are two things here , 1. Calling the whole method here will give access of each var. 
                            #2. IF we only want to call the variables then in the method 1 i.e def series1(self) , I will define each variable as self.num, self,num1 etc. Means One should give reference of each variable
    
    
c=fibonacci_series()
c.series2()