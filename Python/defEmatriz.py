# vetorExemplo = ['texto', 'texto1', 'texto2', 'texto3', 'texto4', 'texto5', 'texto6']
#
# for i in range(0, len(vetorExemplo)):
#   print(vetorExemplo[i])

# matrizExemplo = [['um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete'],
#                  ['oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze'],
#                  ['quinze', 'dezeseis', 'dezesete', 'dezoito', 'dezenove', 'vinte', 'vinte e um']]
#
# for linha in range(0, len(matrizExemplo)):
#   for coluna in range(0, len(matrizExemplo[0])):
#     print(f'{[matrizExemplo[linha][coluna]]} ', end='')
#     print("\n")

# matrizMultExemplo =  [
#                         [
#                           ['a', ['b1', 'b2']],
#                           ['c', 'd']
#                         ],
#                         [
#                           ['e', 'f'],
#                           ['g', 'h']
#                         ]
#                       ]
# print(f'{[matrizMultExemplo[0][0][1][0]]}', end='')

# vetorPython = [1, 2.5, 'teste']
#
# for item in vetorPython:
#   print(item)
#   print(type(item)) #mostra o tipo do elemento

def criaMatriz(linhas, colunas):
  mat = [0] * linhas
  for i in range(linhas):
    mat[i] = [0] * colunas
  print(mat)
  return mat

def populaMatriz(matriz, linhas, colunas):
  for l in range(0, linhas):
    for c in range(0, colunas):
      matriz[l][c] = int(input('Digite o valor da linha ['+str(l)+'] coluna ['+str(c)+']: '))

def mostraMatriz(matriz, linhas):
  for i in range(linhas):
    print(matriz[i][:])


if __name__ == '__main__':
  linhas = int(input('Digite o número de linhas: '))
  colunas = int(input('Digite o número de colunas: '))
  matriz = criaMatriz(linhas, colunas)
  populaMatriz(matriz, linhas, colunas)
  mostraMatriz(matriz, linhas)


