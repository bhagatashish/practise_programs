'''
# decorators means defining function inside a function
def plusone(number):
    def add(number):
        number= number+1
        return number
    result = add(number)  
    print(result)
plusone(2)

# Passing Functions as Arguments to other Functions
def plus_one(number):
    return number + 1
    print(number)
def function_call(function):
    number_to_add = 5
    return function(number_to_add)
'''    
    
    
# another simple eg 
class abc:
    def exec_function1(self,a):
        print("hello")
        y=1
        a=1+y
        self.a=a
        print(a)
        return self
        
        
    @exec_function1
    def cube(a):
        return a
        
        
        
        
    
abc.cube(3)


'''

    
def square(b):
    
        return b**2
        print("square is of b in "+ str(b))

        



def exec_function(i,j): # its just like paasing exec_function(cube,3)
    return i(j)

print(exec_function(cube,3))




''' 