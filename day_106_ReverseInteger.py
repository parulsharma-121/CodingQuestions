'''
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21

'''
def reverse(x):
    if (x == 0):
        return 0
    
    if (x > 0):
        x = str(x)
        x = x[::-1]
        x = int(x) if int(x) <= pow(2,31) else 0
        return x
    
    elif (x < 0):
        x = str(x)
        x = '-'+ x[1:][::-1]
        x = int(x) if int(x) >= -pow(2,31) - 1 else 0
        return x
x = 124
print(reverse(x))