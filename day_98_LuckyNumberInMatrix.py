'''
Given a m * n matrix of distinct numbers, return all lucky numbers in the matrix in any order.

A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.

 

Example 1:

Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
Output: [15]
Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column
Example 2:

Input: matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
Output: [12]
Explanation: 12 is the only lucky number since it is the minimum in its row and the maximum in its column.

'''
def luckyNumbers (matrix):
    row = len(matrix)
    column = len(matrix[0])
    res=[]
    for i in range(row):
        for j in range(column):
            if(matrix[i][j] == min(matrix[i]) and matrix[i][j] == max([matrix[k][j] for k in range(row)])):
                res.append(matrix[i][j])

    return res
matrix = [[3,7,8],[9,11,13],[15,16,17]]
print(luckyNumbers(matrix))