import numpy as np
import sys

n = int(input('Tamaño de la matriz: '))
matrix = np.zeros((n, n + 1))
solution = np.zeros(n)

print('Ingrese los coeficientes:')
for i in range(n):
    for j in range(n + 1):
        matrix[i][j] = float(input('[' + str(i) + '][' + str(j) + ']='))
print('\n Matriz: \n',matrix)

for i in range(n):
    if matrix[i][i] == 0.0:
        sys.exit('Error (0/0)')
    for j in range(n):
        if i != j:
            ratio = matrix[j][i] / matrix[i][i]
            for k in range(n + 1):
                matrix[j][k] = matrix[j][k] - ratio * matrix[i][k]

for i in range(n - 1, -1, -1):
    for j in range(i - 1, -1, -1):
        ratio = matrix[j][i] / matrix[i][i]
        for k in range(n + 1):
            matrix[j][k] = matrix[j][k] - ratio * matrix[i][k]

for i in range(n):
    temp = matrix[i][i]
    for j in range(n + 1):
        matrix[i][j] = matrix[i][j] / temp

for i in range(n):
    solution[i] = matrix[i][n]

print('\nSolucion al sistema: ')
for i in range(n):
    print('X%d= %0.2f' % (i, solution[i]), end='\t')