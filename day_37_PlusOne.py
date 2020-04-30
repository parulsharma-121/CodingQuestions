'''
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.


'''

def plusOne(digits):
    res = []
    for i in range(len(digits)):
        digits[i]=str(digits[i])
    num = int(''.join(digits)) + 1


    for i in range(len(str(num))):
        res.append(str(num)[i])
    
    return res

digits = [1,2,3]
print(plusOne(digits))