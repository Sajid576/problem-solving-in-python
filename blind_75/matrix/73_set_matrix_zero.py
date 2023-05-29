
from typing import List

def setZeroes( matrix: List[List[int]]) -> None:
    row,col=len(matrix),len(matrix[0])
    
    
    zeroContainColumn={} # THIS WILL TRACK COLUMNS WHICH HAS 0
    
    for r in range(row):
        flag=0                # flag=1 INDICATES CURRENT ROW CONTAINS 0
        for c in range(col):
            
            if (matrix[r][c]==0):
                flag=1
                zeroContainColumn[c]=True
        
        if (flag):            # flag=1 INDICATES CURRENT ROW CONTAINS 0, SET ENTIRE ROW TO 0
            matrix[r]=[0]*col


    for r in range(row):
        for c in range(col):
            if (c in  zeroContainColumn):
                matrix[r][c]=0
        
        
    return matrix

print(setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))
