def soma_das_matrizes(matriz1, matriz2):

 if len(matriz1) != len(matriz2) or len(matriz1[0]) != len(matriz2[0]):
   raise ValueError ("A matrizes devem ter as mesmas dimensões.")


 matriz_resultante = []

 for linha in range(len(matriz1)):
     linha_resultante = []
     for coluna in range(len(matriz1[0])):
        soma = matriz1[linha][coluna] + matriz2[linha][coluna]
        linha_resultante.append(soma)
     matriz_resultante.append(linha_resultante)

 return matriz_resultante

matriz1 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

matriz2 = [[9, 8, 7],
           [6, 5, 4],
           [3, 2, 1]]
   
 

resultado = soma_das_matrizes(matriz1, matriz2)
 
print(resultado)