def isAlpha(c):
        if((c >='a' and c<='z') or (c>='A' and c<='Z')or (c>='0' and c<='9')):
            return True
        else:
            return False

def isPalindrome(self, s: str) -> bool:
        res1=''
        res2=''
        i=0
        j=len(s)-1
        while(j>0 or i< len(s) ):
            if(self.isAlpha(s[i])):
                res1+=(s[i].lower())
            if(self.isAlpha(s[j])):
                res2+=(s[j].lower())
            i+=1
            j-=1

        
        
        if(res1==res2):
            return True
        else:
            return False