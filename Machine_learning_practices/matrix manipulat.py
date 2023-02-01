matrix = [[2,5,8],
          [4,6,8],
          [5,7,10]]
rows, cols = len(matrix), len(matrix[0])
new_matrix = [[0]*rows for i in range(cols)]

a =0
while a< len(matrix[0]):

    for i in range(len(matrix[0])):
        new_matrix[a][i]= matrix[i][a]
    a += 1
print(new_matrix)
print(matrix)

