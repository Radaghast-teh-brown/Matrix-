A = [[1],[2]]
B = [[5,5,5,5]]
C = list()
for i in range(len(A)):
    listaTemporaria = list()
    for k in range(len(B[0])):
        soma = 0
        for j in range(len(A[0])):
            soma += A[i][j]*B[j][k]
        listaTemporaria.append(soma)
    C.append(listaTemporaria)

for i in C:
    print(i)
