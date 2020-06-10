'''
Given two strings representing two complex numbers.

You need to return a string representing their multiplication. Note i2 = -1 according to the definition.

Example 1:
Input: "1+1i", "1+1i"
Output: "0+2i"
Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.
Example 2:
Input: "1+-1i", "1+-1i"
Output: "0+-2i"
Explanation: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert it to the form of 0+-2i.

'''
def complexNumberMultiply(a, b):
    a = a.split('+')
    b = b.split('+')
    
    a1 = int(a[0])
    b1 = int(b[0])
    
    a2 = int(a[1].replace('i', ''))
    b2 = int(b[1].replace('i', ''))
    
    real = a1*b1 - a2*b2
    
    imaginary = a1*b2 + b1*a2
    
    return '{}+{}i'.format(real, imaginary)
 
a="1+1i" 
b="1+1i"
print(complexNumberMultiply(a,b))