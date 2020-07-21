'''
You have a list of points in the plane. Return the area of the largest triangle that can be formed by any 3 of the points.

Example:
Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
Output: 2
Explanation: 
The five points are show in the figure below. The red triangle is the largest.

'''
def largestTriangleArea(points):
    res = 0
    N = len(points)
    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            for k in range(i + 2, N):
                (x1, y1), (x2, y2), (x3, y3) = points[i], points[j], points[k]
                res = max(res, 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)))
    return res
points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
print(largestTriangleArea(points))
        