import math
import string
def main():
    t=input()
    n=len(t)
    dem=0
    left=0
    ok=0
    for x in t:
        if x=='1':
            if left==0:
                left=1
            else:
                if ok==1:
                    dem+=1
                    ok=1
                    left=0
        else:
            if x=='0':
                ok=1
            else:
                ok=0
            
    print(dem)        
if __name__ == "__main__":
    main()        