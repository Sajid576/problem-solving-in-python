def LCSubStr(X, Y, m, n):
    # LCSuff is the table with zero
    # value initially in each cell
    LCSuff = [[0 for k in range(n+1)] for l in range(m+1)]
 
    # To store the length of longest common substring
    result = 0
     
    highest_length_indx=(0,0)
    # Following steps to build
    # LCSuff[m+1][n+1] in bottom up fashion
    for i in range(m + 1):
        for j in range(n + 1):
            if (i == 0 or j == 0):
                LCSuff[i][j] = 0
            elif (X[i-1] == Y[j-1]):
                LCSuff[i][j] = LCSuff[i-1][j-1] + 1
                if(result<=LCSuff[i][j]):
                        result = LCSuff[i][j]
                        highest_length_indx=(i,j)
            else:
                LCSuff[i][j] = 0

    # backtracking to get the substring
    i=highest_length_indx[0]
    j=highest_length_indx[1]
    elem=LCSuff[i][j]
    lcs=''
    while(elem!=0):       
        lcs+=X[i-1]
        i=i-1
        j=j-1
        elem=LCSuff[i][j]
       

    return result,lcs
 
 
# Driver Code
X = 'cbbd'
Y = X[::-1]
print(X,Y)
m = len(X)
n = len(Y)
 
len,lcs=LCSubStr(X, Y, m, n)
print("\nLCS , LCS length")
print(lcs,len)