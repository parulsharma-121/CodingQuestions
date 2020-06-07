'''
Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.  Return a list of all possible strings we could create.

Examples:
Input: S = "a1b2"
Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

Input: S = "3z4"
Output: ["3z4", "3Z4"]

Input: S = "12345"
Output: ["12345"]

'''
def letterCasePermutation(S):
    for i in S:
        curr =[""]
        for i in range(len(S)):
            result = []
            if (S[i].isdigit()):
                for j in curr:
                    result.append(j + S[i])
            else:
                for j in curr:
                    result.append(j + S[i].upper())
                    result.append(j + S[i].lower())
            curr = result
    return curr

S = "a1b2"
print(letterCasePermutation(S))