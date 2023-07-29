from typing import List

def rotate( matrix: List[List[int]]) -> None:

    # transpose the matrix
    # reverse every row

    for r in range(len(matrix)):
        for c in range(r):
            matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
                
        
    for r in range(len(matrix)):
            matrix[r].reverse()
            
        
        return matrix
            
            
    
    return matrix

print(rotate([[1,2,3],[4,5,6],[7,8,9]]))