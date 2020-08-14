'''
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example 1:

Input: 16
Output: true
Example 2:

Input: 5
Output: false


'''
def isPowerOfFour(num):
    return num > 0 and not num & (num - 1)  and len(bin(num)) % 2 
num = 16
print(isPowerOfFour(num))
        