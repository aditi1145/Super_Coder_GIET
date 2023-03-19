'''
#substrings
n1=int(input())
n2=int(input())

result=[]
array=[k for k in range(n1,n2+1)]

print(array)

for i in range(len(array)):
    for j in range(i,len(array)):
        result.append(array[i:j+1])
print(result)

#substrings using list comprehension
result=[array[i:j+1] for i in range(len(array)) for j in range(i,len(array))]
print(result)

result=[i if(i%2!=0) else i**2 for i in range(11)]
print(result)

x=[[1,2,3],[21,22,45],[8,9,6]]
result2=[j**2 if(j%2!=0) else j**3 for i in range(len(x)) for j in x[i]]
print(result2)

mylist=[9,6,1,5,0,8,2,4,7]
list_b=[6,4,6,1,2,3]
ans=[(i,mylist.index(i)) if(i in mylist) else (i,"not in mylist") for i in list_b ]
print(ans)

mylist=[9,6,1,5,0,8,2,4,7]
list_b=[6,4,6,1,2,3]
ans={k:v for (k,v) in zip(mylist,list_b)}
print(ans)

mylist=[9,6,1,5,0,8,2,4,7]
list_b=[6,4,6,1,2,3]
ans={i:mylist.index(i) if(i in mylist) else "not in mylist" for i in list_b }
print(ans)

sentences=["a new world recored was set",
           "in the holy city of ayodhya",
           "on the eve of diwali on teusday",
           "with over three lakh diya or eastern lamp",
           "lit up simultaneously on the banks of the sarayu river"]
stopwords=["for","a","of","the","and","to","in","on","with","was","or"]
res=[i for j in sentences for i in j.split(" ") if(i not in stopwords) ]
print(res)

sentence='a new world recored'
x=sentence.lower()
res=[ord(i)-96 if(i !=' ' ) else i for i in x]
print(res)

num1=0

l=[int(i) for i in input().split(',')]
for i in range(len(l)):
    if(i>=l.index(5) and i<=l.index(8)):
        pass
    else:
        num1=num1+l[i]
num2=int(''.join([str(i) for i in l[l.index(5):l.index(8)+1]]))
print(num2+num1)


s,n=input().split(':')
nn=sum([int(i)**2 for i in list(n)])
if(nn%2==0):
    print(s[len(s)-1]+s[:len(s)-1])
else:
    print(s[2:]+s[:2])
    
'''
'''

            
 
def prime(i):
    c1=0
    for z1 in range(2,int(i**0.5)+1):
        if(i%z1==0):
            c1=1
    if c1==0:
        return True
    else:
        return False
        
def f(m):
    for i in range(2,m+1):
        if(m%i==0):
            if(prime(i)):
                z=i
        
    return z
l=0    
n=int(input())
for i in range(9):
    l=l+f(n+i)
print(l)
'''
