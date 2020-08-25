'''
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

'''
def isPalindrome(x):
    y =str(x)
    if(x<0):
        return False
    elif(y==y[::-1]):
        return True
    else:
        return False
x = 121
print(isPalindrome(x))