import math


def main():
    k=int(input())
    n=int(input())
    s=[]*n
    for i in range (n):
        x=input().strip()
        s.append(x)
    a=input().strip()
    
    m=len(a)
    if k>m:
        print(0)
        return
    dem=0
    frex=a[:k]
    for i in range(n):
        if s[i][:k]==frex:
            dem+=1
    print(dem)
if __name__ == "__main__":
    main()



