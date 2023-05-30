from typing import List

def rotate( matrix: List[List[int]]) -> None:
    n = len(matrix)

    for i in range(0,n):
        j=n-1
        while(j>0):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp
            j-=1
        
            
            
    
    return matrix

print(rotate([[1,2,3],[4,5,6],[7,8,9]]))