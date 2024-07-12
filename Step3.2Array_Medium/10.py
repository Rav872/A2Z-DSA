# Set matrix to zeroes
# Brute force method
# optimal solution will be marking rows and columns in separate arrays


matrix = [[1,1,1],[1,0,1],[1,1,1]]

row = len(matrix)
column = len(matrix[0])
rowList = [0]*row
columnList = [0]*column
# if matrix[i][j] is 0 mark rowList[i] = 1, columnList[j] = 1
# for 1->rowlen
# for j -> colLen
# if rowlist[i] == 1 or columnList[j]  == 1 make matrix[i][j] = 0


def markRow(i):
    for j in range(row):
        if matrix[i][j] == 1:
            matrix[i][j] = -1

def markColumn(j):
    for i in range(column):
        if matrix[i][j] == 1:
            matrix[i][j] = -1
        
for i in range(row):
    for j in range(column):
        if matrix[i][j] == 0:
            markRow(i)
            markColumn(j)

for i in range(row):
    for j in range(column):
        if matrix[i][j] == -1:
            matrix[i][j] = 0

print(matrix)