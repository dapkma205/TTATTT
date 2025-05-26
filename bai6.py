import math

def xu_ly(a, w, p):
    m = math.ceil(math.log2(p))
    t = math.ceil(m / w)
    A = []
    while t >= 1 :
        temp = 2**(t*w - w)
        A.append(a // temp)
        a -= temp * A[-1]
        t -= 1
    return A
def cong(a,b,w):
    t = len(a)
    mod = 2**w
    c = [0]*t
    e=0
    for i in range(t):
        tong = a[i]+b[i]+e
        if tong>= mod :
            e=1
        else:
            e=0
        c[i]=tong % mod
    return e,c;
        
a = int(input())
b =int (input())
w = int(input())
p = int(input())
A= xu_ly(a, w, p)
B= xu_ly(b,w,p)
carry ,c = cong(A,B,w)
print("Kết quả cộng: (", carry, ",", tuple(c), ")")
