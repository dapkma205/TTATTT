import math


def match(a,b):
    n=len(a)
    m=len(b)
    if m!=n:
        return False
    dd=[0]*266
    for i in range (n):
        if dd[ord(a[i])]==0:
            dd[ord(a[i])]=ord(b[i])
        else:
            if dd[ord(a[i])]!=ord(b[i]):
                return False
    return dd


def main():
    n=int(input())
    s=[]*n
    for i in range(n):
        x=input().strip()
        s.append(x)
    a=input().strip()
    
    for i in range(n):
        if match(a,s[i]):
            print(s[i],end=" ")
            
            
if __name__ == "__main__":
    main()
