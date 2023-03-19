class Customer:
    def __init__(self, v):
        self.__qt=0
        self.__cname=''
        self.__type=''
    def set_cname(self,nmc):
        self.__cname=nmc
    def set_quantity(self,qtc):
        self.__qt=qtc
    def validate_quantity(self):
        return (self.__qt in range(1,6))
    def getname():
        return self.__cname

class Pizzaservice:
    counter=100
    def __init__(self,obj):
        self.__objc=obj
        self.__cost=0
        self.__s=[]
   
    def set_type(self,ty):
        self.__type=ty
    def validate_type(self):
        print(self.type=="small" or self.type=="medium")
    add_top=bool(input("Enter 1 to add toppings,else enter 0 for no toppings:"))
    def calculate_cost(self):
        cost=(150 if(self.type=="small") else 200)
        if(add_top and self.type=="small"):
            self.__cost+=35
        elif(add_top and self.type=="medium"):
            self.__cost+=50
        else:
            self.__cost=-1
        Pizzaservice.counter+=1
        self.id=self.type[0]+str(Pizzaservice.counter)
        return [self.id,self.pcost,self.type,add_top]

    if(__objc.validate_quantity() and validate_type()):
        self.__s=calculate_cost()
    def getcost(self):
        return self.__cost()
    def getname1():
        return __objc.getname()
    
class Doordelivery:
        
     def __init__(self,ovj):
         self.dist=0
         self.__ovjc=ovj
         self.pcost=0
     
     def setdis(self,dis):
         self.dist=dis
        
     def validate_dist_km(self):
        return(self.dist in range(1,11))
    
         
        
     def pizcost(self):
        self.pcost=__ovjc.getcost()
        if(self.dist<=5):
            self.pcost+=5*self.dist
            return self.pcost+5     
        elif(self.dist in range(6,11)):
            self.pcost+=7*self.dist
            return self.pcost
        else:
            self.pcost=-1
            
    if(validate_dist_km() and self.pcost!=-1):
        pizcost()
        display()
        print("Thank you for buying pizza!.Your pizza will be delivered at your doorsteps in 40 mins!!")
    else:
        print("distance out of range,pizza cost=",self.pcost)
            
     
            
     def display(self):
        s=__ovjc.calculate_cost()
        print("Customer Name:",__ovjc.getname1)
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
        print("delivery charges",self.pcost - __ovjc.getcost())
        print("Total cost= :",self.pcost)  
 
    

nmc=input("Enter your name Name:")
obj=Customer()
obj.set_cname(nmc)
qtc=int(input("Enter number of pizzas:"))
obj.set_quantity(qtc)


for i in range(qtc):
    obj1=Pizzaservices()
    typev=input("Enter size(Available sizes:small and medium):").lower()
    obj1.set_type(typev)
    
    if(choice==0):
        msg="Thank you for buying pizza!.your pizza will be ready at our center in 40 mins!! at rupees="
        Doordelivery.display(obj1,msg)
           
    else:
        
        di=int(input("enter distance in kilometers"))
        obj3.setdis(di)
        

            

