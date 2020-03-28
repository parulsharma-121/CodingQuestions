#to lower case

def toLowerCase(self, str):
        
        ns=''
        for i in str:
            if(90>=ord(i)>=65 ):
                ns+=chr(ord(i)+32)
            else:
                ns+=chr(ord(i))
        return ns
