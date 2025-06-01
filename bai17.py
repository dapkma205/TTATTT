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
    if a<=3:
        return True
    x=random.randint(2,a-1)
    if binh_phuong_co_lap(x,a-1,a) != 1:
        return False  
    return True

def main():
    n=int(input())
    arr=list(map(int, input().split()))
    arr2=[]
    for x in arr:
        if x not in arr2:
            arr2.append(x)
    for x in arr2:
        if fermat(x):
            print(x, end=' ')
            
if __name__ == "__main__":
    main()
     