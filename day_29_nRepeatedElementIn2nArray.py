'''
In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.

Return the element repeated N times.

 

Example 1:

Input: [1,2,3,3]
Output: 3
Example 2:

Input: [2,1,2,5,3,2]
Output: 2

'''

def repeatedNTimes(A):
    freq=dict()
    for i in A:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    for k,v in freq.items():
        if(v==int(len(A)/2)):
            return k

A = [1,2,3,3]
print(repeatedNTimes(A))