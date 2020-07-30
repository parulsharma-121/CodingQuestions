'''
Given an array A of 0s and 1s, consider N_i: the i-th subarray from A[0] to A[i] interpreted as a binary number (from most-significant-bit to least-significant-bit.)

Return a list of booleans answer, where answer[i] is true if and only if N_i is divisible by 5.

Example 1:

Input: [0,1,1]
Output: [true,false,false]
Explanation: 
The input numbers in binary are 0, 01, 011; which are 0, 1, and 3 in base-10.  Only the first number is divisible by 5, so answer[0] is true.
Example 2:

Input: [1,1,1]
Output: [false,false,false]
Example 3:

Input: [0,1,1,1,1,1]
Output: [true,false,false,false,true,false]

'''
def prefixesDivBy5(A):
    q = 0
    ans = []
    for x in A:
        if q == 0:
            q = (0 if x==0 else 1)
        elif q==1:
            q = (2 if x==0 else 3)
        elif q==2:
            q = (4 if x==0 else 0)
        elif q==3:
            q = (1 if x==0 else 2)
        else:
            q = (3 if x==0 else 4)
        ans.append(True if q==0 else False)
    return ans
A = [0,1,1]
print(prefixesDivBy5(A))