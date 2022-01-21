#Contagem inteligente (exercício 01):

início = int(input('Digite o início da contagem: '))
final = int(input('Digite o final da contagem: '))

if início < final:
    print('\nResultado da contagem:', end=' ')
    
    for n in range(início, final +1):
        print(n, end=' ')

elif início > final:

    print('\nResultado da contagem:', end=' ')

    cont = início
    
    while cont > final - 1:
        print(cont, end=' ')
        cont -= 1
