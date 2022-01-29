#Ex02: Analisador de Valores.

def números():

    soma = contador = contador_null = soma_pares = 0
    
    for n in range(1, 6):
        número = int(input(f'Digite o {n}ª valor: '))

        soma += número
        média = soma / 5

        if número % 5 == 0:
            contador += 1

        if número == 0:
            contador_null += 1

        if número % 2 == 0:
            soma_pares += número

    print(f'\nA soma entre os valores é igual a: {soma}.\nA média entre os valores e igual a: {média}.\n{contador} número (s) é (são) divisível (eis) por 5.')
    print(f'{contador_null} números são nulos.\nA soma entre os valores pares e igual a: {soma_pares}.')

números()
