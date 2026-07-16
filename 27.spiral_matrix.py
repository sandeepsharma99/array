def spiralOrder(matrix) :
        
        m = len(matrix) # row
        n = len(matrix[0]) # col
        
        result = []

        sr,er = 0,m-1
        sc,ec = 0,n-1

        while sr<=er and sc<=ec:

            if not matrix:
                return []

            for col in range(sc,ec+1):
                result.append(matrix[sr][col])
            sr+=1
            
            for row in range(sr,er+1):
                result.append(matrix[row][ec])
            ec-=1
            
            if sr<=er:
                for col in range(ec,sc-1,-1):
                    result.append(matrix[er][col])
                er-=1
            
            if sc<=ec :
                for row in range(er,sr-1,-1):
                    result.append(matrix[row][sc])
                sc+=1
                
        return result

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(spiralOrder(matrix))

