import math


p=int(input())
q=int(input())
e=int(input())


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


def rsa(p,q,e):
    phin=(p-1)*(q-1)
    return nghich_dao_mod(e,phin)[1]%phin
print(p*q)
print(rsa(p,q,e))