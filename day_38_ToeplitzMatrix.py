'''
A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.

Now given an M x N matrix, return True if and only if the matrix is Toeplitz.
 

Example 1:

Input:
matrix = [
  [1,2,3,4],
  [5,1,2,3],
  [9,5,1,2]
]
Output: True
Explanation:
In the above grid, the diagonals are:
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
In each diagonal all elements are the same, so the answer is True.

'''

def isToeplitzMatrix(matrix):
        
    n = len(matrix)
    n1 = len(matrix[0])
    for i in range(n):
        for j in range(n1):
            if i > 0 and j > 0 and matrix[i][j] != matrix[i-1][j-1]:
                return False
    return True

matrix = [
  [1,2,3,4],
  [5,1,2,3],
  [9,5,1,2]
]
print(isToeplitzMatrix(matrix))