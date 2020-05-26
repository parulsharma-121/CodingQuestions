'''
Given a positive integer num, output its complement number. The complement strategy is to flip the bits of its binary representation.

 

Example 1:

Input: num = 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
Example 2:

Input: num = 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.

'''
def findComplement(num):
    bin_no=bin(num)[2:]
    n=len(bin_no)
    res=0
    for i in range(0,n):
        if(bin_no[i]=="0"):
            res+=2**(n-1-i)
    return res
num = 5
print(findComplement(num))