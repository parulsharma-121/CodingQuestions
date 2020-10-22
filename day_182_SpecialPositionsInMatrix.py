'''
Given a rows x cols matrix mat, where mat[i][j] is either 0 or 1, return the number of special positions in mat.

A position (i,j) is called special if mat[i][j] == 1 and all other elements in row i and column j are 0 (rows and columns are 0-indexed).

 

Example 1:

Input: mat = [[1,0,0],
              [0,0,1],
              [1,0,0]]
Output: 1
Explanation: (1,2) is a special position because mat[1][2] == 1 and all other elements in row 1 and column 2 are 0.

'''
def numSpecial(mat):
    count = 0
    for i in mat:
        if sum(i) <= 1:
            for j in range(len(mat[0])):
                if(i[j] == 1):
                    r = i[:]
                    c = [x[j] for x in mat]
                    if (sum(r)+sum(c) == 2):
                        count += 1
    return count
mat = [[1,0,0],[0,0,1],[1,0,0]]
print(numSpecial(mat))