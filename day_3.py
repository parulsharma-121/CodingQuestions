 # Generate a String With Characters That Have Odd Counts

def generateTheString(self, n):
       y='p'*(n-1)
       if(n%2==0):
           y+='z'
       else:
           y+='p'
        
       return y
