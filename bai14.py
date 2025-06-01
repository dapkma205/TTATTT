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
    
 
def binh_phuong_co_lap(m,e,n):
    """m mu e mod n"""
    A=m
    b=1
    while e!=0:
        if e%2!=0:
            b=(b*A)%n
        A=(A*A)%n
        e=e//2
    return b

    
def elgamal(a,x,k,p,apha):
    beta=binh_phuong_co_lap(a,apha,p)
    gama=binh_phuong_co_lap(apha,k,p)
    xichma=((x-a*gama)*nghich_dao_mod(k,p-1)[1])%(p-1)
    return gama,xichma

p=int(input())
apha=int(input())
a=int(input())
k=int(input())
x=int(input())
gama,xichma=elgamal(a,x,k,p,apha)
print(gama,xichma)