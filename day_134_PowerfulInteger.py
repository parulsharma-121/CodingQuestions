'''
Given two positive integers x and y, an integer is powerful if it is equal to x^i + y^j for some integers i >= 0 and j >= 0.

Return a list of all powerful integers that have value less than or equal to bound.

You may return the answer in any order.  In your answer, each value should occur at most once.

 

Example 1:

Input: x = 2, y = 3, bound = 10
Output: [2,3,4,5,7,9,10]
Explanation: 
2 = 2^0 + 3^0
3 = 2^1 + 3^0
4 = 2^0 + 3^1
5 = 2^1 + 3^1
7 = 2^2 + 3^1
9 = 2^3 + 3^0
10 = 2^0 + 3^2
Example 2:

Input: x = 3, y = 5, bound = 15
Output: [2,4,6,8,10,14]
'''
def powerfulIntegers(x, y, bound):
    a=0
    b=0
    res=[]
    if x==1 and y==1:
        if bound>=2:
            res.append(2)
    elif x==1:
        while y**b+1<=bound:
            res.append(y**b+1)
            b+=1
    elif y==1:
        while x**a+1<=bound:
            res.append(x**a+1)
            a+=1
    else:  
        while x**a+1<=bound:
            if x**a+y**b<=bound:
                res.append(x**a+y**b)
                b+=1
            else:
                a+=1
                b=0
    return list(set(res))
x = 2
y = 3
bound = 10
print(powerfulIntegers(x,y,bound))
        