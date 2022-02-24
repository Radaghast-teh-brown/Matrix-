from Matriz import Matriz

matrizA = [[1,1],[2,2]]
matrizB = [[2,2],[2,2]]
A = Matriz(matrizA)
C = A.produto(matrizB)
for i in C:
    print(i)