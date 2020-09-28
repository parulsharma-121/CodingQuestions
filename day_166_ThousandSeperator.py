'''
Given an integer n, add a dot (".") as the thousands separator and return it in string format.

 

Example 1:

Input: n = 987
Output: "987"
Example 2:

Input: n = 1234
Output: "1.234"
Example 3:

Input: n = 123456789
Output: "123.456.789"

'''
def thousandSeparator(n):
    s1 = str(n)
    s2= s1[::-1]
    s3 = '.'.join(s2[i:i+3] for i in range(0, len(s2), 3))
    res = s3[::-1]
    return res 
n = 123467
print(thousandSeparator(n))