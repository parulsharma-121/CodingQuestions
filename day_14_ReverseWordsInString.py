'''
Given a string, you need to reverse the order of characters in each 
word within a sentence while still preserving whitespace and initial word order.

Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
'''


from typing import List
def reverseWords(s: str) -> str:
        inp_lst = s.split()
        out_lst = []
        for i in inp_lst:
            out_lst.append(i[::-1])
            
        return ' '.join(out_lst)

s = "Let's take LeetCode contest"
print(reverseWords(s))