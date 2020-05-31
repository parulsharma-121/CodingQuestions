'''
Given a positive integer N, find and return the longest distance between two consecutive 1's in the binary representation of N.

If there aren't two consecutive 1's, return 0.

 

Example 1:

Input: 22
Output: 2
Explanation: 
22 in binary is 0b10110.
In the binary representation of 22, there are three ones, and two consecutive pairs of 1's.
The first consecutive pair of 1's have distance 2.
The second consecutive pair of 1's have distance 1.
The answer is the largest of these two distances, which is 2.


'''
def binaryGap(N):
    n = bin(N)
    p1 = 0
    p2 = 0
    d = 0

    for i in range(2, len(n)):
        if(n[i] == '1'):
            if(p1 == 0):
                p1 = i
            else:
                p2 = i
                d = max((p2-p1), d)
                p1 = p2
        
    return d

N = 22
print(binaryGap(N))