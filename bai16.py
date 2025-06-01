from encodings.punycode import T
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
def fermat(n,a):
    if binh_phuong_co_lap(a, n-1, n) != 1:
        return False
    return True


def main():
    n=int(input())
    t=int(input())
    kq=0
    for i in range(t):
        a=int(input())
        if fermat(n,a)==False:
            kq+=1
    if kq==0:
        print(-1)
    else:
        print(kq)
if __name__ == "__main__":
    main()

    