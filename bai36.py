import string


def ktra(s,mau):
    k=len(s)
    h=len(mau)
    j=0
    for i in range(k):
        if s[i]>='A' and s[i]<='Z':
            if j==h:
                return 'false'
            else:
                if s[i]==mau[j]:
                    j+=1
                else:
                    return 'false'
    return 'true'
def main():
    n=int(input())
    s=[]
    for i in range(n):
        x=input().strip()
        s.append(x)
    mau=input().strip()
    for i in range (n):
        print(ktra(s[i],mau))

if __name__ == "__main__":
    main()    