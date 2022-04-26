import itertools
class Reverse:
    def reverse_string(self):
        a = ['nitin','subash','susu']
        b = []
        j=0
        reverse=[]
        list= []
        list3=[]
        for i in a :
            print[i]
            
            
            name= a[j]
            j=j+1
            
            print(name)
            name=[i for i in name]
            reverse= [j for j in reversed(name)]
           
            if name==reverse:
                print("palindrome")
            else:
                print("not palindrome")
            name.clear()
            reverse.clear()
            '''
            for x,k in zip(name,reversed(name)):
            
                list.append(x)
                reverse.append(k)
                
            print(list)
            print(reverse)
            if list==reverse:
                print(name + ' is palindrome')
            else :
                print(name +' is not palindrome')
            list.clear()
            reverse.clear()
            '''
    
    def reverse_number(self):
        num = 1234
        print(1234%10)
        reverse=0
        while(num > 0):
            reminder = num%10
            reverse=(reminder*10)+reminder
            num=num//10
        print(reminder,reverse)
            
            
Reverse.reverse_number('')
Reverse.reverse_string("")