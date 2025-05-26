import math
def nghichdao(a,b):
    u=a
    v=b
    x1=1
    x2=0
    while u!=1:
        q=v//u
        r=v-q*u
        x=x2-q*x1
        v=u
        u=r
        x2=x1
        x1=x
    if x1<0:
        return x1+b
    return x1
def mod_china(k,a,n):
    N=1
    for i in range (k):
        N=N*n[i]
    x=0
    for i in range (k):
        M=N//n[i]
        inv=nghichdao(M,n[i])
        x+=a[i]*M*inv
    return x%N

k=int(input())
a=[0]*k  
n=[0]*k     
for i in range (k):
    a[i],n[i]=map(int,input().split())
print(mod_china(k,a,n))
    
