'''
Given a string s. You should re-order the string using the following algorithm:

Pick the smallest character from s and append it to the result.
Pick the smallest character from s which is greater than the last appended character to the result and append it.
Repeat step 2 until you cannot pick more characters.
Pick the largest character from s and append it to the result.
Pick the largest character from s which is smaller than the last appended character to the result and append it.
Repeat step 5 until you cannot pick more characters.
Repeat the steps from 1 to 6 until you pick all characters from s.
In each step, If the smallest or the largest character appears more than once you can choose any occurrence and append it to the result.

Return the result string after sorting s with this algorithm.

'''
def sortString(s):
    s = list(s)
    ans = ''
    while(s):
        for i in sorted(set(s)):
            s.remove(i)
            ans += i
        for i in sorted(set(s), reverse=True):
            s.remove(i)
            ans += i
    return ans

s = "aaaabbbbcccc"
print(sortString(s))