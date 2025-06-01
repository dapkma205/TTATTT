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
 
 
def fermat(a):
    if a<2:
        return False
    if a<=2:
        return True
    x=random.randint(2,a-1)
    if binh_phuong_co_lap(x,a-1,a) != 1:
        return False  
    return True



a=int(input())
b=int(input())
sum=0
for i in range(a,b+1):
    if fermat(i):
        sum+=i
print(sum)

