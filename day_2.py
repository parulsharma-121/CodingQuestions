def subtractProductAndSum(self, n):
        y=[int(i) for i in str(n)]
        add=0
        prod=1
        for i in y:
            add=add+i
            prod=prod*i
            
       
            
        return prod-add
