'''
#next palindrome number
import sys
def nextpali(n):
    m=int(n)
    for i in range(m+1,sys.maxsize):
        if(str(i)==str(i)[::-1]):
            print(i)
            break
n=input()
nextpali(n)

#frequent disease
d={"P":"Pediatrics","O":"Orthopedics","E":"ENT"}
pat=input().split(',')
max=0
for i in d.keys():
    x=pat.count(i)
    if(x>max):
        max=x
        c=i
print(d[c])   

#string containing common chars in s1 string and s2 string
x=input()
y=input()
a=set(x)
b=set(y)
m=[]
for i in a:
    if(i in b and i!=' '):
        m.append(i)
print(''.join(m))
 
#STRING CORRECTNESS
def chck(n,m):
    c=0
    for i in range(len(n)):
        if(n[i]!=m[i]):
            c=c+1
    return c
    
def find_correct(d):
    c=0
    ac=0
    w=0
    for i in d.keys():
        if(d[i]==i):
            c=c+1
        elif(len(d[i])!=len(i)):
            w=w+1
        else:
            if(chck(i,d[i])>2):
                w=w+1
            else:
                ac=ac+1
    l=[c,ac,w]
    return l

d={"their":"their",
    "business":"bisiness",
    "windows":"windmill",
    "were":"eaew",
    "sample":"sample"}
    
print(find_correct(d))
    
 
#longest substring overlap
def check(w1,w2,i,j):
    c=0
    for k in range(len(w1)-i):
        if(j+k<len(w2) and w1[i+k]==w2[j+k]):
            c=c+1
        else:
            break
    
    data=[c,i]
    return(data)  
        
w1,w2=input().split(',')
st=[]
for i in range(len(w1)):
    for j in range(len(w2)):
        if(w1[i]==w2[j]):
            st.append(check(w1,w2,i,j))
            
       
ma=max(st,key=lambda x:x[0])

print(w1[ma[1]:ma[1]+ma[0]])
        
'''

