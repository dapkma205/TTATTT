

def ktra(s,goal):
    if len(s)!=len(goal):
        return 'false'
    n=len(s)
    for i in range (n):
        s=s[1:]+s[0]
        if s==goal:
            return 'true'
    return 'false'

def main():
    s=input().strip()
    goal=input().strip()
    print(ktra(s,goal))
    
if __name__ == "__main__":
    main()    