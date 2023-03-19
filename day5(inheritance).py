class Customer:
    def __init__(self):
        self.qt=None
    
    def setqt(self,n):
        self.qt=n
        
    def validate_quantity(self):
        return (self.qt in range(1,6))
    


class Pizzaservice(Customer):
    counter=100
    
    def __init__(self):
        self.type=None
        self.pcost=0
        self.id=None
        
    def validate_type(self,ty):
        self.type=ty
        if(self.type=="small" or self.type=="medium"):
            return True    
        else:
            return False
    
    def cost(self):
        add_top=bool(int(input("enter 0-no toppings or 1-adding toppings : ")))
        if(self.type=="small"):
            self.pcost=150
            if(add_top):
                self.pcost+=35
                
        else:
            self.pcost=200
            if(add_top):
                self.pcost+=50
        Pizzaservice.counter+=1
        self.id=self.type[0]+str(Pizzaservice.counter)
        return [self.id,self.pcost,self.type,add_top]
        

class Doordelivery(Pizzaservice):
    
     def __init__(self):
         self.dist=0

     def setdis(self,dis):
         self.dist=dis
        
     def validate_dist_km(self):
        if(self.dist in range(1,11)):
            return True
        else:
            return False
        
     def pizcost(self,pizcost):
        self.pcost=pizcost
        if(self.dist<=5):
            self.pcost+=5*self.dist
            return self.pcost+5     
        elif(self.dist in range(6,11)):
            self.pcost+=7*self.dist
            return self.pcost
        else:
            self.pcost=-1
            return self.pcost
        
     def display(self,s,cost,sum1,cn):
        print("Customer Name:",cn)
        print("Order details:\n")
        print("Total number of pizzas ordered:",len(s))
        print("\n")
        for k in range(len(s)):
            print("pizza id :",s[k][0])
            print("size     :",s[k][2])
            if(s[k][3]==True):
                x="Present"
            else:
                x="Absent"
            print("toppings :",x)
            print("pizza cost:",s[k][1])
            print("\n")
        print("delivery charges",sum1-cost)
        print("Total cost= :",sum1)
        
            
            
cus=input("Enter customer name:")     
pizcost=0
loe=[]
obj=Customer()
qty1=int(input("enter number of pizza (1 or 2 or 3 or 4 or 5): "))
obj.setqt(qty1)
x=obj.validate_quantity()
if(x):
    obj2=Pizzaservice()
    for i in range(qty1):
        print("enter size of pizza(small or medium) of pizza",i+1,end=': ')
        ty=input()
        y=obj2.validate_type(ty)
        
        if(x and y):
            list1=obj2.cost()
            loe.append(list1)
    print(loe)
    for j in range(qty1):
        pizcost=pizcost+loe[j][1]
    choice=int(input("Enter 0 for collecting at shop or 1 for door delivery :"))
    
    if(choice==0):
        obj3=Doordelivery()
        obj3.display(loe,pizcost,pizcost,cus)
        print("Thank you for buying pizza!.your pizza will be ready at our center in 40 mins!! at rupees=",pizcost)
        
    else:
            obj3=Doordelivery()
            di=int(input("enter distance in kilometers"))
            obj3.setdis(di)
            print("\n")
            if(obj3.validate_dist_km() and pizcost!=-1):
                obj3.display(loe,pizcost,obj3.pizcost(pizcost),cus)
                print("Thank you for buying pizza!.Your pizza will be delivered at your doorsteps in 40 mins!!")
            else:
                print("distance out of range,pizza cost=",obj3.pizcost(pizcost))

else:
    print("Caution:You can at max order 5 pizzas!!")
