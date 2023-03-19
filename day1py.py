#python programming.
'''
#correct decision making is very important.
n=int(input())
if(n%3==0 and n%5==0):
    print("multiple of 3 and 5")
elif(n%3==0):
    print("multiple of 3")
elif(n%5==0):   
    print("multiple of 5")
else:
    print("invalid")

#even odd sequencial printing of numbers in normal,reverse order

for i in range(1,101):
    print(i,end=',')
print("\n")
for i in range(2,101,2):
    print(i,end=',')
print("\n")
for i in range(1,101,2):
    print(i,end=',')
print("\n")
for i in range(100,0,-1):
    print(i,end=',')
print("\n")
for i in range(100,0,-2):
    print(i,end=',')
print("\n")
for i in range(99,0,-2):
    print(i,end=',')

#break-to stop when a particular condition is satisfied.

for i in range(1,101):
    if(i==50):
        break
    print(i,end=',')

#continue:to skip the activity if the condition is satisfied and continue looping if the condition is unsatisfied

for i in range(1,101):
    if(i==50):
        continue
    print(i,end=',')


def funct1(num):
    return(print(56))
print(type(funct1(56)))#type none


def func(a,b):
    print(str(a)+b)
print(20.3,'10')
    
def func(a,b):
    print(a+str(b))
print('20.3',10)

def func(a,b):
    print(a+float(b))
print(20.3,'10')
 
def func(a,b):
    print(float(a)+b)
print(10,20)

#missing positional argument4(only shows error if no. of arguments passed is less do not check data type)
 #TypeError: fun() missing 1 required positional argument: 'c'
def fun(a,b,c):
    print(float(a)+b)
fun(10,20)
#TypeError: fun() takes 3 positional arguments but 4 were given
def fun(a,b,c):
    print(float(a)+b)
fun(10,20,30,40)

#2 keyword arguments:

def fun(a,b,c=10):#keyword2
    print(float(a)+b+c)
fun(b=20,a=40)#keyword1


#error:non default arguments follow default argument.
def fun(a=40,b,c):#keyword2
    print(float(a)+b+c)
fun(20,30)#keyword1

#default values taken from right to left

def fun(*var):#tuple=
    for i in var:
        print(i,end=( " "))
fun(10,20)
print()

fun(10,20,30)
print()

fun(10,20,30,40)


def fun(*var):#tuple=
    sum=0
    for i in var:
        sum=sum+i
    print(sum)
fun(10,20)
print()

fun(10,20,30)
print()

fun(10,20,30,40)


def fun(*var):
    c=0
    sum=1
    for j in var:
        c=c+1
        if(j==7):
            
            break
        else:
            sum=sum*j
    if(c==1):
        return(-1)
    else:
        return(sum)

l=list(map(int,input().split(',')))
num1=l[0]
num2=l[1]
num3=l[2]
print(fun(num3,num2,num1))

#CURRENCY CALCULATOR
need=int(input("specified indian currency"))
c=int(input("1 for euro,2 for british pound,3 for australian dollar,4 for canadian dollar"))
if(c==1):
    print(need*0.01417,"INR")
elif(c==2):
    print(need*0.0100,"INR")
elif(c==3):
    print(need*0.02140,"INR")
elif(c==4):
    print(need*0.02027,"INR")
else:
    print(-1)

rpa=37550.0
rpc=float(1/3 * rpa)
tax=0.07
l=list(map(int,input().split(' ')))
np=l[0]
nc=l[1]
dis=0.1
ta=rpa*np+rpc*nc
fta=ta+tax*ta
print("Final Ticket Amount",fta-(dis*fta))

#one line code:
l=list(map(int,input().split(' ')))
np=l[0]
nc=l[1]

print("Final Ticket Amount",(((((37550.0*np+12516.666666666666*nc)*1.07)*0.9))))


l=list(map(int,input().split(' ')))
a1=l[0]
a5=l[1]
am=l[2]
c=0
if(am!=0):
    if(am>=5):
        c=c+1
        am=am-5
    elif(am<5 and am!=0):
    
        
print(a1,' ',c)
'''
