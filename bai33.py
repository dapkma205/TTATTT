import math

def dem_chu(p):
    dd=[0]*256
    n=len(p)
    for i in range(n):
        dd[ord(p[i])]+=1
    return dd
def xu_li(s,p):
    n=len(s)
    m=len(p)
    dd1=dem_chu(p)
    kq=[]
    for i in range(n-m+1):
        cn=s[i:i+m]
        dd2=dem_chu(cn)
        if dd1==dd2:
            kq.append(i)
    return kq

def main():
    s=input().strip()
    p=input().strip()
    kq=xu_li(s,p)
    for i in range(len(kq)):
        print(kq[i],end=" ")
        

if __name__ == "__main__":
    main()  
    