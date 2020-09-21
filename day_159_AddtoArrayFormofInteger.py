'''
For a non-negative integer X, the array-form of X is an array of its digits in left to right order.  For example, if X = 1231, then the array form is [1,2,3,1].

Given the array-form A of a non-negative integer X, return the array-form of the integer X+K.

 

Example 1:

Input: A = [1,2,0,0], K = 34
Output: [1,2,3,4]
Explanation: 1200 + 34 = 1234
Example 2:

Input: A = [2,7,4], K = 181
Output: [4,5,5]
Explanation: 274 + 181 = 455

'''
def addToArrayForm(A, K):
    list_to_int = lambda A: int(''.join(str(i) for i in A)) # Generator exp.
    A1 = list_to_int(A) + K
    return list(str(A1))
A = [1,2,0,0]
K = 34
print(addToArrayForm(A,K))
        