import math

def last_occurrence(p):
    l=[-1]*256
    n=len(p)
    for i in range(n):
        l[ord(p[i])]=i
    return l

def boyer_moore(t,p):
    n=len(t)   
    m=len(p)
    L=last_occurrence(p)
    if n<m:
        return -1
    i=m-1
    j=m-1
    while i<n:
        if t[i]==p[j]:
            i=i-1
            j=j-1
            if j<0:
                return i+1
        else:
            dem=0
            i=i+m-min(j,1+L[ord(t[i])])
            j=m-1
    return -1



def main():
    s=input().strip()
    p=input().strip()
    s=s[::-1]
    p=p[::-1]
    kq=boyer_moore(s,p)
    if kq==-1:
        print(-1)
        return
    print(len(s)-len(p)-kq+1)
    




if __name__ == "__main__":
    main()