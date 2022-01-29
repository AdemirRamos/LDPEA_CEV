#Ex01: Analisador de Valores.

def números():

    contador = soma_ímpares = soma_ímpares_010 = 0
    
    for n in range(0, 6):
        número = int(input('Digite um número: '))
    
        if número > 0 and número < 10:
            contador += 1

        if número % 2 == 1:
            soma_ímpares += número

        if número % 2 == 1 and número > 0 and número < 10:
            soma_ímpares_010 += número

    print()
    print(f'Entre os valores digitados, {contador} está (ão) entre 0 e 10.')
    print(f'A soma entre todos os valores ímpares é igual a: {soma_ímpares}.')
    print(f'A soma entre os valores impares (entre 0 e 10) é igual a: {soma_ímpares_010}.')
        
números()
