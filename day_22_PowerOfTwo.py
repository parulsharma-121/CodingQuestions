

def isPowerOfTwo(n: int) -> bool:
    if(n==0):
        return False
    while(n!=1):
        n=n/2
        if(n%2!=0 and n!=1):
            return False
        
    return True


n = 28
isPowerOfTwo(n)