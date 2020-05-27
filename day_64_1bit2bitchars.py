'''
We have two special characters. The first character can be represented by one bit 0. The second character can be represented by two bits (10 or 11).

Now given a string represented by several bits. Return whether the last character must be a one-bit character or not. The given string will always end with a zero.

Example 1:
Input: 
bits = [1, 0, 0]
Output: True
Explanation: 
The only way to decode it is two-bit character and one-bit character. So the last character is one-bit character.


'''
def isOneBitCharacter(bits):
    n = len(bits)
    j = 0
    for i in range(n-2,-1,-1):
        if(bits[i]==1):
            j+=1
        else:
            break
    if(j%2==0):
        return True
    return False

bits = [1,0,0]
print(isOneBitCharacter(bits))