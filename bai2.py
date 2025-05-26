import math
p=int(input())
q=int(input())
e=int(input())
m=int(input())
n=q*p
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
print(binh_phuong_co_lap(m,e,n))
        
            
        
        
