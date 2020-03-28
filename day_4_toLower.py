'''
Implement function ToLowerCase() that has a string parameter str, and 
returns the same string in lowercase.
Input: "Hello"
Output: "hello"

Input: "here"
Output: "here"
'''

def toLowerCase(my_string:str)->str:        
        ns=''
        for i in my_string:
            if(ord(i)<=90 and ord(i)>=65 ):
                ns+=chr(ord(i)+32)
            else:
                ns+=chr(ord(i))
                
        return ns

my_string='Hello'

print(toLowerCase(my_string))