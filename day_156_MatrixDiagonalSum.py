'''
Given a square matrix mat, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.

 

Example 1:


Input: mat = [[1,2,3],
              [4,5,6],
              [7,8,9]]
Output: 25
Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
Notice that element mat[1][1] = 5 is counted only once.
Example 2:

Input: mat = [[1,1,1,1],
              [1,1,1,1],
              [1,1,1,1],
              [1,1,1,1]]
Output: 8
Example 3:

Input: mat = [[5]]
Output: 5

'''
def diagonalSum(mat):
    a=0
    if len(mat[0])%2==0:
        for i in range(len(mat[0])):
            a+=mat[i][i]
            a+=mat[i][len(mat[0])-1-i]
    else:
        for i in range(len(mat[0])):
            a+=mat[i][i]
            a+=mat[i][len(mat[0])-1-i]
        a=a-mat[len(mat[0])//2][len(mat[0])//2]
    return a
mat = [[1,2,3],[4,5,6],[7,8,9]]
print(diagonalSum(mat))