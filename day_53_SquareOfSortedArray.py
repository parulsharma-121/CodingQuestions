'''
Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.

 

Example 1:

Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Example 2:

Input: [-7,-3,2,3,11]
Output: [4,9,9,49,121]


'''
def sortedSquares(A):
    lst = []
    for i in A:
        lst.append(i**2)
        
    return sorted(lst)

A = [-1,2,-4,5,6]
print(sortedSquares(A))