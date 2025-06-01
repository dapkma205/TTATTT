import math

def xu_li(s):
    dd=[0]*266
    vv=['u','e','o','a','i']
    for i in range(5):
        dd[ord(vv[i])]=1
    n=len(s)
    na=0
    pa=0
    hoi=0
    for i in range(n):
        if s[i]!="?":
            if dd[ord(s[i])]==1:
                na+=1
                pa=0
            else:
                pa+=1
                na=0
        else:
            na+=1
            pa+=1
        if pa>3 or na>5:
            return "BAD"
    return "GOOD"

def main():
    s=input().strip()
    print(xu_li(s))


if __name__ == "__main__":
    main()
    
        



