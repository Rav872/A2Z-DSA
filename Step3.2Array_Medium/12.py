# spiral traverse of a matrix

matrix = [[1, 2, 3, 4],
		  [5, 6, 7, 8],
		  [9, 10, 11, 12],
	      [13, 14, 15, 16]]

row = len(matrix[0])
column = len(matrix)

top, Left = 0
Right, bottom = row
result = []
while top <= bottom and left <= right:
    for i in range(right):
        result.append(matrix[top][i])
        top += 1
    for i in range(left):
        result.append(matrix[i][right])
        right += 1
    for i in range()
        

