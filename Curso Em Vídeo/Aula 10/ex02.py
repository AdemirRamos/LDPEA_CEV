#Ex02: Seletor de Pessoas.

def menu():

    contador_homem = 0
    contador_mulher = 0
    
    while True:
        print()
        sexo = str(input('Qual o sexo? ')).lower().strip()[0]
        idade = int(input('Qual a idade? '))
        
        print('\n[1] Preto\n[2] Castanho\n[3] Loiro\n[4] Ruivo\n')
        
        hair = int(input('Qual a cor do cabelo? '))
        
        opção = str(input('\nVocê quer continuar? [Sim / Não]: ')).lower().strip()[0]
        
        if sexo == 'm' and idade > 18 and hair == 2:
            contador_homem += 1

        elif sexo == 'f' and idade >= 25 and idade <= 30 and hair == 3:
            contador_mulher += 1
            
        if opção == 'n':
            break

    print(f'\nO número de homens com mais de 18 anos e cabelo castanho é de: {contador_homem}.')
    print(f'O número de mulheres loiras entre 25 e 30 anos de idade é de: {contador_mulher}.')

menu()
