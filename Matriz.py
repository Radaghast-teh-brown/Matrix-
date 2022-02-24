class Matriz:
    def __init__(self, matriz):
        self.__matriz = list(matriz)
        self.__linhas = len(matriz)
        self.__colunas = len(matriz[0])
    @property
    def linhas(self):
        return self.__linhas 
    @property
    def colunas(self):
        return self.__colunas

    def ordem(self):
        return str(self.__linhas ) + "X" + str(self.__colunas)
    def isQuadrada(self):
        if self.__linhas == self.__colunas:
            return True 
        return False
    def produto(self, matrizB):
        if( self.__colunas == len(matrizB)):
            matrizC = list()
            for i in range(self.__linhas):
                listaTemporaria = list()
                for k in range(len(matrizB[0])):
                    soma = 0
                    for j in range(self.__colunas):
                        soma += self.__matriz[i][j]*matrizB[j][k]
                    listaTemporaria.append(soma)
                matrizC.append(listaTemporaria)
            return matrizC
            
        else:
            print("Não é possível fazer produto das matrizes")
        




