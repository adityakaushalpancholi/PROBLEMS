
# SO THIS THE PROGRAM FOR JUST TRANSPPOSING THE MATRIX NOT ROTATING IT 90 DEGREE

a = [[1, 2, 3], 
     [4, 5, 6], 
     [7, 8, 9]]
row = len(a)
colm = len(a[0])
result = [ [0]*row for _ in range(colm)] 
for i in range(0,row):
    for j in range(0,colm):
        result[j][i] = a[i][j]
a = []
for row in result:
    x = list(reversed(row))
    a.append(x)
print(a)
    




