'''
class Vehicle:
    def __init__(self):
        self.__id=0
        self.__type=""
        self.__cost=0
        self.__pre=0
    def setid(self,idv):
        self.__id=idv
    def settype(self,typev):
        self.__type=typev
    def setcost(self,costv):
        self.__cost=costv
        
    
    def premam(self):
        if(self.__type=="two wheeler"):
            self.__pre=self.__cost*0.02
        elif(self.__type=="four wheeler"):
            self.__pre=self.__cost*0.06
        
    def gettype(self):
        print("type=",self.__type)
    def getid(self):
        print("id=",self.__id)
    def getcost(self):
        print("cost=",self.__cost)
    def getpremam(self):
        print("premium amount=",self.__pre)


typev=input("Enter two wheeler or four wheeler")
if(typev=='two wheeler' or typev=='four wheeler' ):
    idv=int(input("input vehicle id"))
    costv=int(input("enter cost"))
    obj=Vehicle()
    obj.setid(idv)
    obj.settype(typev)
    obj.setcost(costv)
    obj.premam()
    obj.gettype()
    obj.getid()
    obj.getcost()
    obj.getpremam()
    
else:
    print("vehicle type is invalid!!")
  
class Student:
    
    def __init__(self):
        self.__student_id=None
        self.__marks=None
        self.__age=None
        self.__cid=None
        self.__quali="Not Qualified"
        self.__fees=0
        
    def setid(self,idv):
        self.__student_id=idv
    def setage(self,agev):
        self.__age=agev
    def setmarks(self,marksv):
        self.__marks=marksv
        
    def validate_marks(self):
        return (self.__marks>=0 and self.__marks<=100)
    
    def validate_age(self):
        return self.__age>20
  
    def check_qualification(self,x1,y1):
        if((x1 and y1) and self.__marks>=65):
            self.__quali="Qualified"
            print("Congratulations you are Qualified!!")
            return True
        else:
            #print("Candidate is not qualified.")
            return False
    def getid(self):
        print("student id:  ",self.__student_id)
    def getage(self):
        print("age:  ",self.__age)
    def getmarks(self):
        print("marks:  ",self.__marks)
        
    def choose_course(self):
        self.__cid=input("enter course id 1001 or 1002 ")
        if(self.__cid=='1001'):
            self.__fees=25575.00
        elif(self.__cid=='1002'):
            self.__fees=15500.00
        else:
            print("Invalid Input")
    
        if(self.__marks>85):
            self.__fees=self.__fees-(0.25*self.__fees)
        print("Qualifications:  ",self.__quali)
        print("course id:  ",self.__cid)
        print("fees:  ",self.__fees)
        
obj=Student()

idv=int(input("enter id:"))
marksv=int(input("enter marks:"))
agev=int(input("enter age:"))
x=False
y=False
obj.setid(idv)
obj.setmarks(marksv)
obj.setage(agev)
x=obj.validate_marks()
y=obj.validate_age()
obj.getid()
obj.getage()
obj.getmarks()

if(obj.check_qualification(x,y)):
    obj.choose_course()
 '''   
            

