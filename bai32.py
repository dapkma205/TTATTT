import math
import string



def xu_li(s):
    n=len(s)
    k=n//2
    str1=""
    str2=""
    dem=0
    for i in range(k):
        str1=str1+s[i]
        str2=s[n-i-1]+str2
        if str1==str2:
            dem=i+1
    return dem
def main():
    
    s=input()
    kq=xu_li(s)
    print(kq)

if __name__ == "__main__":
    main()  
    
    
        
        
        
    

    
    
    