import math

def xu_li(s, p):
    n = len(s)
    m = len(p)
    
    dd = [[False] * (n + 1) for _ in range(m + 1)]
    dd[0][0] = True

    
    for i in range(1, m + 1):
        if p[i - 1] == "*":
            dd[i][0] = dd[i - 1][0]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[i - 1] == "*":
                dd[i][j] = dd[i - 1][j] or dd[i][j - 1]
            elif p[i - 1] == '?' or p[i - 1] == s[j - 1]:
                dd[i][j] = dd[i - 1][j - 1]
            else:
                dd[i][j] = False

    return dd[m][n]  

def main():
    s = input().strip()
    p = input().strip()
    if xu_li(s, p):
        print("true")
    else:
        print("false")

if __name__ == "__main__":
    main()
