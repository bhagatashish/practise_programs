from different_programs.Fibonacci_series import fibonacci_series


class class2(fibonacci_series):
    def series1(self,num):
        self.num =num
        print(self.num)
       
    def series2(self):
        return self.series1(123)          
        
        
c = class2
c.series2()