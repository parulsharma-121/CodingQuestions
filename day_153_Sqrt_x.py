'''
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since 
             the decimal part is truncated, 2 is returned.

'''
def mySqrt(x):
    if(x == 1):
        return 1
    mid = x // 2
    while True:
        if(mid*mid > x):
            high = mid
            mid //=2

        else:
            low = mid +1
            if(low*low > x):
                return mid
            else:
                mid = (high+mid)//2
x = 4
print(mySqrt(x))
