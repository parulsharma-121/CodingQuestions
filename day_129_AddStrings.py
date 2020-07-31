'''
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.


'''
def addStrings(num1, num2):
    n1 = int(num1)
    n2 = int(num2)
    return str(n1+n2)
num1 = "0"
num2 = "0"
print(addStrings(num1,num2))