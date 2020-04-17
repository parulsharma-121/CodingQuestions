def checkPerfectNumber(num):
    if(num==1):
        return False
    res=1
    x=2
    while(x*x<=num):
        if(num%x==0):
            res=res+x+(num/x)
        x+=1
    if(res==num):
        return True
    else:
        return False


num=28
print(checkPerfectNumber(num))