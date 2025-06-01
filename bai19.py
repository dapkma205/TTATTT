import math
import random

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


def miller_rabin(n,t):
    if n<2:
        return False
    if n<=3:    
        return True
    s,r=get_s_r(n)
    for i in range(t):
        a=random.randint(2,n-2)
        y=binh_phuong_co_lap(a,r,n)
        if y!=1 and y!=n-1:
            j=1
            while j<=s-1 and y!=n-1:
                y=(y*y)%n
                if y==1:
                    return False
                j=j+1
            if y!=n-1:
                return False  
    return True
def main():
    a=int(input())
    b=int(input())
    sum=0
    for x in range(a,b+1):
        if miller_rabin(x,1):
            sum+=x
    print(sum)
if __name__ == "__main__":
    main()