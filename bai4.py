import math
p, g = map(int, input().split())
a, b= map(int, input().split())
def mod(a,b,c):
    """a^b mod c"""
    A=a
    e=b
    b=1
    while e!=0:
        if e%2!=0:
            b=(b*A)%c
        A=(A*A)%c
        e=e//2
    return b
A=mod(g,a,p)
B=mod(g,b,p)
K=mod(A,b,p)
print(K)