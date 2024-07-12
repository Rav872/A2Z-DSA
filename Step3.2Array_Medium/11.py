#Rotate matrix 90*
 
#matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
row = len(matrix[0])
column = len(matrix)
result = [[0]*row for i in range(column)]
for j in range(column):
    for i in range(row-1, -1,-1):
        r = j % column
        k = (row-1) - (i % row)
        result[r][k] = matrix[i][j]
        
print(result)