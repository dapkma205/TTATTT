import math
p=int(input())
g=int(input())
y=int(input())
k=int(input())
m=int(input())
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
a=binh_phuong_co_lap(g,k,p)
b=(binh_phuong_co_lap(y,k,p)*m)%p
print(a)
print(b)
# 211
# 39
# 108
# 29
# 34
    