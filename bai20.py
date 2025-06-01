import math
import random
from re import A

def binh_phuong_co_lap(m, e, n):
    """m mu e mod n"""
    A = m
    b = 1
    while e != 0:
        if e % 2 != 0:
            b = (b * A) % n
        A = (A * A) % n
        e = e // 2
    return b

def get_s_r(n):
    r=n-1
    s=0
    while(r%2==0):
        r//=2
        s+=1
    return s,r


def miller_rabin(n,r,a,jmax):
    
    y=binh_phuong_co_lap(a,r,n)
    if y!=1 and y!=n-1:
        j=1
        while j<=jmax and y!=n-1:
            y=(y*y)%n
            if y==1:
                return y
            j=j+1
        if y!=n-1:
            return y 
    return "Too many steps"


def main():
    n=int(input())
    r=int(input())
    a=int(input())
    jmax=int(input())
    kq= miller_rabin(n,r,a,jmax)
    print(kq)
if __name__ == "__main__":
    main()