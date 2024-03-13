def inverte_niveis_arvore(arvore_array):
    def inverte_niveis_arvore(arvore_array, index):
        if index < 0:
            return arvore_array

        index_direito = 2 * index + 2
        index_esquerdo = 2 * index + 1

        if index_direito < len(arvore_array) and index_esquerdo < len(arvore_array):
            arvore_array[index_direito], arvore_array[index_esquerdo] = arvore_array[index_esquerdo], arvore_array[index_direito]

        return inverte_niveis_arvore(arvore_array, index - 1)

    return inverte_niveis_arvore(arvore_array, len(arvore_array) - 1)


entrada = [int(numero) for numero in input().split(' ')]
arvore_array_invertido = inverte_niveis_arvore(entrada)
resultado = ' '.join(f'{numero}' for numero in arvore_array_invertido)
print(resultado)
