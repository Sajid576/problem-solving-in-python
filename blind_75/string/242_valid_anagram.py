
def isAnagram( s: str, t: str) -> bool:
        mapping={}
    
        if(len(s)!=len(t)):
            return False
        
        for i in range(len(s)):
            if(s[i] not in mapping):
                mapping[s[i]]=1
            else:
                mapping[s[i]]+=1
            
        
        for i in range(len(t)):
            if(t[i] in mapping):
                mapping[t[i]]-=1
                if(mapping[t[i]]==0):
                    mapping.pop(t[i])
            else:
                return False
        return len(mapping)==0