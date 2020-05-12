'''
Given an array A of integers, for each integer A[i] we may choose any x with -K <= x <= K, and add x to A[i].

After this process, we have some array B.

Return the smallest possible difference between the maximum value of B and the minimum value of B.

 

Example 1:

Input: A = [1], K = 0
Output: 0
Explanation: B = [1]
'''
def smallestRangeI(A,K):
    length = len(A)
    maxim = max(A)
    minm = min(A)
    diff = abs(max(A)-min(A))
    if(length==1):
        return 0
    if(diff>=2*K):
        minm +=K
        maxim -=K
        return abs(maxim-minm)
    else:
        return 0
    A = [1]
    K = 0
    print(smallestRangeI(A,K))