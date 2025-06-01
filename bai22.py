import math
import string


def last_occurrence(p):
    l=[-1]*256
    n=len(p)
    for i in range(n):
        l[ord(p[i])]=i
    return l

def boyer_moore(t,p):
    n=len(t)   
    m=len(p)
    kq=[]
    L=last_occurrence(p)
    if n<m:
        return -1
    i=m-1
    j=m-1
    while i<n:
        if t[i]==p[j]:
            if j==0:
                kq.append(i+1)
                i=i+m
                j=m-1
            i=i-1
            j=j-1
        else:
            dem=0
            i=i+m-min(j,1+L[ord(t[i])])
            j=m-1
    return kq

def main():
    t=input()
    p=input()
    kq=boyer_moore(t,p)
    if len(kq)>0:
        for i in kq:
            print(i, end=' ')
    else:
        print(-1)
if __name__ == "__main__":   
    main()  