#Estruturas Condicionais (Parte 1)

#Condicional Simples: condicional de apenas uma possibilidade.

#Condicional Composta: condicional com mais de uma possibilidade.

#Exercícios práticos:

#1ª: Carteira de motorista:

ano = int(input('Digite o ano atual: '))
nascimento = int(input('Digite o seu ano de nascimento: '))
cálculo = ano - nascimento
print(f'Você tem {cálculo} anos de idade\n')
if cálculo > 18:
    print('Você já pode tirar carteira de motorista.')
else:
    print('Você ainda não pode tirar carteira de motorista.')

#2ª: Média:

print()

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
média = (n1 + n2) / 2
print(f'A sua média foi: {média}.\n')
if média >= 7:
    print('Você foi aprovado.')
else:
    print('Você foi reprovado.')
