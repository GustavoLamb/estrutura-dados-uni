import math

array = input().split()
altura = math.floor(math.log2(len(array)))
elemetos_ultimo_nivel = 2 ** altura
tamanho = len(array) - elemetos_ultimo_nivel
soma = 0

if len(array) != 1:

    for indice in range(len(array) - 1, tamanho - 1, -1):
        if array[indice] != 'None':
            soma += int(array[indice])

print(soma)
