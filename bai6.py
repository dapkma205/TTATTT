import math

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

def order_mod(a, n):
    if math.gcd(a, n) != 1:
        return None
    t = 1
    k = a % n
    while k != 1:
        k = (k * a) % n
        t += 1
    return t


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
def main():
    n=int(input())
    anpha=int(input())
    beta=int(input())
    m=math.sqrt(order_mod(anpha, n))
    m=math.ceil(m)
    a=[0]*m
    b=[0]*m
    for i in range(m):
        a[i]=binh_phuong_co_lap(anpha,i,n)
    for i in range (m):
        b[i]=beta*binh_phuong_co_lap(nghich_dao_mod(anpha,n)[1],m*i,n)%n
    for i in range(m):
        for j in range(m):
            if a[i]==b[j]:
                print(i+m*j)
                return 
            
if __name__ == "__main__":
    main()
            
            

        
    
