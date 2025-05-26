import math

p=int(input())
g=int(input())
x=int(input())
a, b =map(int,input().split())
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


def elgamal(a,b,x):
    tam=binh_phuong_co_lap(a,x,p)
    m=(b*nghich_dao_mod(tam,p)[1])%p
    return m
print(elgamal(a,b,x))