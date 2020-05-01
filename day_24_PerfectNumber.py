'''
We define the Perfect Number is a positive integer that is equal to the sum of all its positive divisors except itself.

Now, given an integer n, write a function that returns true when it is a perfect number and false when it is not.
Example:
Input: 28
Output: True
Explanation: 28 = 1 + 2 + 4 + 7 + 14

'''

def checkPerfectNumber(num):
    if(num==1):
        return False
    res=1
    x=2
    while(x*x<=num):
        if(num%x==0):
            res=res+x+(num/x)
        x+=1
    if(res==num):
        return True
    else:
        return False


num=28
print(checkPerfectNumber(num))