import math

def main():
    s=input().strip()
    dd=[0]*266
    n=len(s)
    for i in range(n):
        dd[ord(s[i])]+=1
    dem=n
    for i in range(0,266):
        if dd[i]!=0:
            dem=dem+dd[i]*(dd[i]-1)//2
    print(dem)
    
if __name__ == "__main__":
    main()