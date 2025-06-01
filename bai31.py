def main():
    s = input("s = ")
    n = len(s)
    kq = False
    
    for i in range(1,n//2+1):  
        if n%i!=0:
            continue  
        
        cn=s[:i]  
        kq=True
        for j in range(0,n,i):
            if s[j:j+i] != cn:
                kq=False
                break
        if kq:
            kq=True
            break

    if kq:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
