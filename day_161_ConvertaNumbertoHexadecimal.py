'''
Given an integer, write an algorithm to convert it to hexadecimal. For negative integer, two’s complement method is used.

Note:

All letters in hexadecimal (a-f) must be in lowercase.
The hexadecimal string must not contain extra leading 0s. If the number is zero, it is represented by a single zero character '0'; otherwise, the first character in the hexadecimal string will not be the zero character.
The given number is guaranteed to fit within the range of a 32-bit signed integer.
You must not use any method provided by the library which converts/formats the number to hex directly.
Example 1:

Input:
26

Output:
"1a"
Example 2:

Input:
-1

Output:
"ffffffff"


'''
def toHex(num):
    dic={}
    dic[10]='a'
    dic[11]='b'
    dic[12]='c'
    dic[13]='d'
    dic[14]='e'
    dic[15]='f'
    ans=''
    if(num<0):
        num=num+2**32
    elif(num==0):
        return '0'
    while(num):
        rem=num%16
        if(rem>=10):
            ans=dic[rem]+ans
        else:
            ans=str(rem)+ans
        num//=16
    return ans
num = 26
print(toHex(num))