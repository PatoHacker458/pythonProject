def ogmatrix():
    n=int(input("Ingrese el tamaño de la matriz: "))
    matrix=[]
    print("COEFICIENTES")
    for i in range(n):
        row=[]
        for j in range(n+1):
            coeficiente=float(input(f"Ingrese el coeficiente ({i+1},{j+1}): "))
            row.append(coeficiente)
        matrix.append(row)
    return matrix

matrix=ogmatrix()
print("Matriz: ")
for row in matrix:
    print(row)