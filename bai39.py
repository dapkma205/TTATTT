def main():
    s=input().split()
    t=input()
    n=len(t)
    for i in range (len(s)):
        tam=s[i][:n]
        if tam==t:
            print(i+1)
            return 
    print(-1)
    

if __name__ == "__main__":
    main()