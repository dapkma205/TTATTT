import math
p=int(input())
a=int(input())
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
print(nghich_dao_mod(a,p)[1]%p)