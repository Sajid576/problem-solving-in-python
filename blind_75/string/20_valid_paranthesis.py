def isValid(s: str) -> bool:
        pairs={
        "(":")",
        "{":"}",
        "[":"]"
            
        }
        stack=[]
        if(len(s)%2!=0):
            return False
        
        for i in range(len(s)):
        
            if(s[i] in pairs):
                stack.append(s[i])
            else:
                if(len(stack)==0):
                    return False
                else:
                    top= stack.pop(-1)
                    if(pairs[top] != s[i]):
                        return False
                
        return len(stack)==0