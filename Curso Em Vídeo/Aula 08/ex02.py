#Exercício número 2: diferença de gols.

time_name_1 = str(input('Digite o nome do primeiro time: '))
time_score_1 = int(input(f'Digite o número de gols do (a) {time_name_1} time: '))
time_name_2 = str(input('\nDigite o nome do segundo time: '))
time_score_2 = int(input(f'Digite o número de gols do {time_name_2} time: '))
cálculo = time_score_1 - time_score_2

if cálculo == 0:
    print('\nEssa foi uma partida normal.')

elif cálculo >= 1 and cálculo <= 3:
    print('\nEssa foi uma vitória tranquila.')

elif cálculo > 3:
    print('\nEssa foi uma goleada.')
