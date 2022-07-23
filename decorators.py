



# decorators without using annotations

def div(a,b):  # this is normal function accepting 2 values
    print(a/b)

def swap_num(func):
    # this function will swap the numbers if required . Hence we are passing a function inside a function
    def inner(a,b): # this inner function is decorator . Without chnaging exiting code , we are consuming other logis
        # logic will be written in another function.
        if a<b:
            a,b = b,a
        return func(a,b) # this will return a func(a,b) to inner function
    return inner # this will return inner function o/p to swap_num
div1 = swap_num(div)

div1(2,4)
#-----------------------------------------------------------------------------------
# same above program with annotations
@swap_num(div(2,4))
def div(a,b):  # this is normal function accepting 2 values
    print(a/b)

def swap_num(func):
    # this function will swap the numbers if required . Hence we are passing a function inside a function
    def inner(a,b): # this inner function is decorator . Without chnaging exiting code , we are consuming other logis
        # logic will be written in another function.
        if a<b:
            a,b = b,a
        return func(a,b) # this will return a func(a,b) to inner function
    return inner # this will return inner function o/p to swap_num





