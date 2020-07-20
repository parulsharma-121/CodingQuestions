'''
Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:

Input: 2.00000, 10
Output: 1024.00000
Example 2:

Input: 2.10000, 3
Output: 9.26100

'''
def myPow(x,n):
    if not n:
        return 1
    
    neg = False
    if(n<0):
        n*=-1
        neg = True

    res = 1
    while n:
        if(n%2==1): 
            res *=x
        x*=x
        n>>=1

    return 1/res if neg else res
x=2.00000
n=10
print(myPow(x,n))
        