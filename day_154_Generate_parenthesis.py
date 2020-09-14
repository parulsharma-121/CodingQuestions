'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

'''
def generateParenthesis(n):
    ss = []
    
    def f(s, left, right):
        if left == n and right == n:
            ss.append(s)
        if left < n:
            f(s+'(', left+1, right)
        if right < n and left > right:
            f(s+')', left, right+1)
    
    f('', 0, 0)
    
    return ss
n = 3
print(generateParenthesis(n))
        