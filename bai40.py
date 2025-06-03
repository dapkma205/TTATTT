def last_occurrence(p):
    l = [-1] * 256
    for i in range(len(p)):
        l[ord(p[i])] = i
    return l

def boyer_moore(t, p):
    n = len(t)
    m = len(p)

    if m == 0 or n < m:
        return -1

    L = last_occurrence(p)
    i = 0

    while i <= n - m:
        j = m - 1
        while j >= 0 and p[j] == t[i + j]:
            j -= 1

        if j < 0:
            return i  
        else:
            bad_char_shift = j - L[ord(t[i + j])]
            i += max(1, bad_char_shift)
    return -1

def main():
    n=int(input())
    s=[]
    for i in range (n):
        x=input()
        s.append(x)
    dem=0
    s.sort(key=len)
    ok=0
    for i in range(n-1):
        for j in range(i+1,n):
            if boyer_moore(s[j],s[i])!=-1:
                print(s[i],end=" ")
                ok=1
    if ok==0:
        print("None")

if __name__ == "__main__":
    main()    