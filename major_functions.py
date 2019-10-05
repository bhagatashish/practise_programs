class programs:
    def join_function(self):
        
        from Tools.scripts.pdeps import printresults
        var1 = "Guru99!"
        var2 = "Software Testing"
        print ("var1[0]:",var1[0])
        print ("var2[1:5]:",var2[1:5]) 
        
        print(var2.join(var1))
        print(var1.join(var1))
        print(var1.join(var2))
        
        print('hello'.join('ah'))
        name = 'guru'
        number = 99
        print('%s %d' % (name,number))
#area of triangle 
    def area_triangle(self):
            height= input("height of the triangle")
            base = input("base of the triangle")
            
            area = (height*base)/2
    def method(self):
        return(self.join_function())
        return(self.area_triangle())
        
           
c=programs()
c.method()


