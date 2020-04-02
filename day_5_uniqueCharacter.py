'''Given a string, find the first non-repeating character in it
 and return it's index. 
 If it doesn't exist, return -1. '''


def firstUniqChar(s: str) -> int:
        my_hash=dict()
        for i in range(len(s)):
            if(s[i] in my_hash):
                my_hash[s[i]] = -1
            else:
                my_hash[s[i]] = i
        
        print(my_hash)
        for x in my_hash.keys():
            if(my_hash[x]>-1):
                return  my_hash[x]
        
        return -1

s = 'leetcode'

print(firstUniqChar(s))