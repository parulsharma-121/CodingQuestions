'''
Every non-negative integer N has a binary representation.  For example, 5 can be represented as "101" in binary, 11 as "1011" in binary, and so on.  Note that except for N = 0, there are no leading zeroes in any binary representation.

The complement of a binary representation is the number in binary you get when changing every 1 to a 0 and 0 to a 1.  For example, the complement of "101" in binary is "010" in binary.

For a given number N in base-10, return the complement of it's binary representation as a base-10 integer.

 

Example 1:

Input: 5
Output: 2
Explanation: 5 is "101" in binary, with complement "010" in binary, which is 2 in base-10.


'''
def bitwiseComplement(N):
    comp = ""
    n = 0
    res = 0
    for i in bin(N)[2:]:
        if(i=="1"):
            comp += "0"
        else:
            comp += "1"
        n+=1
    for i in comp:
        res += int(i)*(2**(n-1))
        n-=1
    return res

N = 5
print(bitwiseComplement(N))