'''
Given a string S that only contains "I" (increase) or "D" (decrease), let N = S.length.

Return any permutation A of [0, 1, ..., N] such that for all i = 0, ..., N-1:

If S[i] == "I", then A[i] < A[i+1]
If S[i] == "D", then A[i] > A[i+1]
 

Example 1:

Input: "IDID"
Output: [0,4,1,3,2]
Example 2:

Input: "III"
Output: [0,1,2,3]


'''
def diStringMatch(S):
    x = 0
    D=len(S)
    result = []
    
    for i in S:
        if (i == 'I'):
            result.append(x)
            x += 1
        else:
            result.append(D)
            D -= 1
            
    if( S[-1] == 'D'):
        result.append(D)
    else:
        result.append(x)
        
    return result
S = "IDID"
print(diStringMatch(S))