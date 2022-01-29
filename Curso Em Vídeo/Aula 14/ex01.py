#Ex01: Confrontos Entre Times.

times = list()

for t in range(0, 3):
    times.append(str(input('Digite o nome do time: ')))

print(f'\nOs times selecionados foram: {times}.')

print('\nJogos:\n')

for t in times:
    for team in times:
        if t != team:
            print(f'Mandante: {t} x Visitante: {team}')
