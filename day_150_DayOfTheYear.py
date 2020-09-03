'''
Given a string date representing a Gregorian calendar date formatted as YYYY-MM-DD, return the day number of the year.

 

Example 1:

Input: date = "2019-01-09"
Output: 9
Explanation: Given date is the 9th day of the year in 2019.
Example 2:

Input: date = "2019-02-10"
Output: 41

'''
def dayOfYear(date):
    s = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    s1 = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    p = 0
    c = False 
    year = int(date[:4])
    m = int(date[5:7])
    d = int(date[-2:])
    if (year % 4) == 0: 
        if (year % 100) == 0: 
            if (year % 400) == 0: 
                c = True
            else: 
                c =  False
        else: 
            c =  True
    else: 
        c =  False
    
    if m == 1:
        return d
    else:
        if c: 
            for i in range(m - 1):
                p += s1[i]
            return p + d
        else:
            for i in range(m - 1):
                p += s[i]
            return p + d
date = "2019-01-09"
print(dayOfYear(date))