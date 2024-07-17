#Merge overlapping subintevals

#intervals=[[1,3],[2,6],[8,10],[15,18]]
intervals=[[1,4], [4,5]]
output = []
rows = len(intervals)-1
columns = len(intervals[0])

for i in range(rows):
    for j in range(1):
        print("Comparing: ", intervals[i][columns-1], " ", intervals[i+1][j])
        if intervals[i][columns-1] >= intervals[i+1][j]:
            newList = [intervals[i][0], intervals[i+1][j+1]]
        else:
            newList = [intervals[i+1][j], intervals[i+1][j+1]]
        output.append(newList)
        
print(output)