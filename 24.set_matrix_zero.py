def setmatrixzero(matrix) :
    m = len(matrix)
    n = len(matrix[0])

    # Arrays to keep track of which rows and columns need to be converted to zero
    row = [0]*m  #  0 = no zero found yet  , 1 = row/column contains a zero
    col = [0]*n
    # Mark rows and columns containing atleast zero
    for i in  range(m) :
        for j in range(n) :
            if matrix[i][j] == 0 :
                row[i] = 1
                col[j] = 1
    # Set cells to zero If the current cell belongs to a marked row or a marked column
    for i in range(m) :
        for j in range(n) :
            if row[i] == 1 or col[j] == 1:
                matrix[i][j] = 0
    
    return matrix


matrix = [[1,1,1],[1,0,1],[1,1,1]]
print(setmatrixzero(matrix))