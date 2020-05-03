'''
Given a matrix A, return the transpose of A.

The transpose of a matrix is the matrix flipped over it's main diagonal,
switching the row and column indices of the matrix.

'''
def transpose(A):
    result = [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]
    return result
A = [[1,2,3],[4,5,6],[7,8,9]]
print(transpose(A))