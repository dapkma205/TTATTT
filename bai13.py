import math
def nghich_dao_mod(a,b):
    if b==0:
        d=a
        x=1
        y=0
        return d,x,y
    d,x1,y1=nghich_dao_mod(b,a%b)
    x=y1
    y=x1-(a//b)*y1
    return d,x,y
    

def eliptic(x1,y1,x2,y2,a,p):
    if x2==x1 and (y1+y2)%p==0:
        return 0,0
    if x1==x2 and y1==y2:
        m=(3*x1*x1+a)*nghich_dao_mod(2*y1%p,p)[1]%p
    else:
        m=(y2-y1)*nghich_dao_mod((x2-x1)%p ,p)[1]%p
    x3=(m*m-x1-x2)%p
    y3=(m*(x1-x3)-y1)%p
    return x3,y3



p=int(input())
a=int(input())
b=int(input())
x1,y1=map(int,input().split())
na=int(input())
x2,y2=x1,y1
for i in range (na-1):
    x2,y2=eliptic(x1,y1,x2,y2,a,p)
print(x2,y2)    