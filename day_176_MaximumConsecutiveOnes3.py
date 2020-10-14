'''
Given an array A of 0s and 1s, we may change up to K values from 0 to 1.

Return the length of the longest (contiguous) subarray that contains only 1s. 

 

Example 1:

Input: A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
Output: 6
Explanation: 
[1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.
Example 2:

Input: A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
Output: 10
Explanation: 
[0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.

'''
def longestOnes(A, K):
    start = 0
    count = 0
    maxSeq = 0
    for i in range(len(A)):
        if(A[i]==0):
            count+=1
        if(count>K):
            if(A[start]==0):
                count-=1
            start += 1
        maxSeq = max(maxSeq,i-start+1)
    return maxSeq

A = [1,1,1,0,0,0,1,1,1,1,0]
K = 2
print(longestOnes(A,K))