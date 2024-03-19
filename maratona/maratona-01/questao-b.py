def inverte_niveis_arvore(arvore_array):
    def inverte_niveis_arvore(arvore_array, index):
        if index < 0:
            return arvore_array

        filho_direito_index = 2 * index + 2
        filho_esquerdo_index = 2 * index + 1

        if filho_direito_index < len(arvore_array) and filho_esquerdo_index < len(arvore_array):
            arvore_array[filho_direito_index], arvore_array[filho_esquerdo_index] = arvore_array[filho_esquerdo_index], arvore_array[filho_direito_index]

            if index % 2 != 0 or index == 0:
                irmao_direito_index = (2 * ((index -1) // 2)) + 2

                irmao_direito_filho_direito = 2 * irmao_direito_index + 2
                irmao_direito_filho_esquerdo = 2 * irmao_direito_index + 1

                valor_filho_direito = arvore_array[filho_direito_index]
                valor_filho_esquerdo = arvore_array[filho_esquerdo_index]

                arvore_array[filho_direito_index], arvore_array[filho_esquerdo_index] = arvore_array[irmao_direito_filho_direito], arvore_array[irmao_direito_filho_esquerdo]
                arvore_array[irmao_direito_filho_direito], arvore_array[irmao_direito_filho_esquerdo] = valor_filho_direito, valor_filho_esquerdo

        return inverte_niveis_arvore(arvore_array, index - 1)

    return inverte_niveis_arvore(arvore_array, len(arvore_array) - 1)


entrada = [int(numero) for numero in input().split(' ')]
arvore_array_invertido = inverte_niveis_arvore(entrada)
resultado = ' '.join(f'{numero}' for numero in arvore_array_invertido)
print(resultado)
