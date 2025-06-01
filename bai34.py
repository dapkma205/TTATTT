import math

def xu_li(s,n,nmax):
    
    dd = [[0 for _ in range(nmax)] for _ in range(256)]
    for i in range(n):
        k=len(s[i])
        for j in range(k):
            x=s[i][j]
            dd[ord(x)][j]+=1
    kq=[]
    for i in range (n):
        k=len(s[i])
        for j in range(k):
            x=s[i][j]
            if dd[ord(x)][j]==1:
                x=s[i][:j+1]
                kq.append(x)
                break
    return kq        
    

def main():
    n=int(input())
    s=[]
    nmax=0
    for i in range(n):
        x=input().strip()
        s.append(x)
        nmax=max(nmax,len(x))
    kq=xu_li(s,n,nmax)
    for i in range(n):
        print(kq[i],end=" ")
    

if __name__ == "__main__":
    main()    