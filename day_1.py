class Solution:
    def isPalindrome(self, x: int) -> bool:
        a=[i for i in str(x)]
        if(a==a[::-1]):
            return True
        else: 
            return False
