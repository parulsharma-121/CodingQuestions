'''
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Follow up: Do not use any built-in library function such as sqrt.

 

Example 1:

Input: num = 16
Output: true
Example 2:

Input: num = 14
Output: false

'''
def isPerfectSquare(num):
    if(num**0.5 == int(num**0.5)):
        return True
    else:
        return False

num = 16 
print(isPerfectSquare(num))