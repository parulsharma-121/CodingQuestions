'''
In a row of seats, 1 represents a person sitting in that seat, and 0 represents that the seat is empty. 

There is at least one empty seat, and at least one person sitting.

Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. 

Return that maximum distance to closest person.

Example 1:

Input: [1,0,0,0,1,0,1]
Output: 2
Explanation: 
If Alex sits in the second open seat (seats[2]), then the closest person has distance 2.
If Alex sits in any other open seat, the closest person has distance 1.
Thus, the maximum distance to the closest person is 2.

'''
def maxDistToClosest(seats):
    begin = end = 0
    if seats[0] == 0:
        idx = 0
        while idx < len(seats) and seats[idx] == 0:
            begin += 1
            idx += 1
        
    if seats[-1] == 0:
        idx = len(seats) - 1
        while idx >= 0 and seats[idx] == 0:
            end += 1
            idx -= 1
        
    long = curr = 0
    for seat in seats:
        if seat == 0:
            curr += 1
            if curr > long:
                long = curr
        else:
            curr = 0
            
    return max(begin, end, (long + 1) // 2)
seats = [1,0,0,0,1,0,1]
print(maxDistToClosest(seats))
        