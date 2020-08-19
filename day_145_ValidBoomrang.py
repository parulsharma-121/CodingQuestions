'''
A boomerang is a set of 3 points that are all distinct and not in a straight line.

Given a list of three points in the plane, return whether these points are a boomerang.

 

Example 1:

Input: [[1,1],[2,3],[3,2]]
Output: true
'''
def isBoomerang(points):
    slope1 = (points[2][1] - points[0][1])*(points[1][0] - points[0][0])
    slope2 = (points[1][1] - points[0][1])*(points[2][0] - points[0][0])

    if(slope1 != slope2):
        return True
    else:
        return False
points = [[1,1],[2,3],[3,2]]
print(isBoomerang(points))