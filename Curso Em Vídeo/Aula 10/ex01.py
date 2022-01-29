def contagem_1(a):
    if a == 1:
        contador = 0
        print()
        print('Resultado da contagem: ', end='')
        while contador < 10:
            contador += 1
            print(f'{contador}', end=' ')

def contagem_2(a):
    if a == 2:
        contador = 11
        print()
        print('Resultado da contagem: ', end='')
        while contador > 0:
            contador -= 1
            print(f'{contador}', end=' ')
            
while True:
    print()
    valor = int(input('\nDigite o valor da contagem [1 (Progressiva), 2 (Regressiva), 3 (Sair do Programa)]: '))
    contagem_1(valor)
    contagem_2(valor)
    if valor == 3:
        break
print('\nFim do programa.')
