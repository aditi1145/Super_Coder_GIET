'''#DAY2 PYTHON OOP
#list:odered-default index
#      datas of diff types can be stored
#      insert update data
#      predefined class
#      data of same type,complex type anything
#      .index(x) .append() .extend([]) .insert(index,value) .pop()(defaultly removes last index,implicitly give index as argument)
#      del [listname]
#string:slicing cutting=s[start:end:step]
#index can  be used by using enumerate(list) idx,value in enumerate(lis)
lis=[10,20,20,30,40]#remove function will remove from last 20
lis2=[10,20,3+2j,'a']
#print(lis,type(lis))
#print(lis2.remove(20)) # output:none
lis2.remove(20)
print(lis2)
lis.remove(20)
print(lis)

x=input()

def check(x):
    a=0
    n=0
    for j in x:
        if(j.isalpha()):
            a=a+1
        elif(j.isnumeric()):
            n=n+1
        else:
            pass
    l=[a,n]
  
    print(l)
check(x)

def find_pairs_of_numbers(l,n):
    c=0
    for i in l:
        for j in l:
            if(i+j == n):
                c=c+1
    if(c):
        return int(c/2)
    else:
        return int(c/2)
    
l=[int(i) for i in input().split(',')]
n=int(input())
print(find_pairs_of_numbers(l,n))


x=input()
l=len(x)
if(l>=2):
    l=[x[0:2],x[-2:]]
    print(''.join(l))
else:
    print(-1)

s=input()
l=len(s)
if(len(s)<3):
    print(s)
elif(s[-3:]=='ing'):
    print(s+'ly')
else:
    print(s+'ing')

def check_double(n):    
    t1=list(n)
    dob=list(str(2*int(n)))
    t1.sort()
    dob.sort()
    if(t1==dob):
        return True
    else:
        return False
    
n=input()
if(int(n)==0):
    print(0)
else:
    print(check_double(n))
#shortcut:if i in str

t=tuple([int(i) for i in input().split(' ')])

t=(20,25,12,15,19,0,0,1,8,10)
m=25
x=list(t)
def find_more_than_avg(x):
    avg=0
    c=0
    avg=sum(x)*0.1
    for i in x:
        if(i>avg):
            c=c+1
    return c*10
def generate_freq(x):
    l=[0]*25
    for j in range(0,25):
        l[j]=x.count(j)
    return l
def sort_marks(x):
    y=[]
    y=x
    y.sort()
    return y
print(find_more_than_avg(x))
print(generate_freq(x))
print(sort_marks(x))

def translate(d,s):
    l=[]
    for i in s:
        l.append(d[i])
    return l

s=input().split()
d={"merry":"god","christmas":"jul","and":"och","happy":"gott","new":"nytt","year":"ar"}

print(translate(d,s))
'''
s=int(input())-1
e=int(input())-1
for i in range(s,e+1):
    x=[]
    for j in range(i,e+1):
        if(j<=i):
            x.append(j)\][[ 
                
    print(x)
        



    







    


    
