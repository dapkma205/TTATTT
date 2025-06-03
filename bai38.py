import math

def last_occurrence(p):
    l = [-1] * 256
    for i in range(len(p)):
        l[ord(p[i])] = i
    return l

def boyer_moore(t, p):
    n = len(t)
    m = len(p)
    kq = []

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
            i += 1
        else:
            bad_char_shift = j - L[ord(t[i + j])]
            i += max(1, bad_char_shift)
    return -1
def main():
    s=input().strip()
    w=input().strip()
    k=boyer_moore(s,w)
    tam=w
    dem=0
    while k!=-1:
        tam=tam+w
        k=boyer_moore(s,tam)
        dem+=1
    print(dem) 

if __name__ == "__main__":
    main()    