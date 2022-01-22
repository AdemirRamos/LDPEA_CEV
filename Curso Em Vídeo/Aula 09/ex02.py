#Maior nota da sala (exercício 02):

contador = 0
maior = 0
nome_maior =  ''

alunos = int(input('Qual a quantidade de alunos? '))
print()
for n in range(0, alunos):
    nome = str(input(f'Nome do (a) {n}ª aluno (a): '))
    nota = int(input('Nota do (a) {n}ª aluno (a): '))
    print()
    
    if nota > maior:
        maior = nota
        nome_maior = nome

    elif maior > nota:
        nota = maior
        
    contador += 1

print(f'O (A) aluno (a) com a maior nota foi: {nome_maior}. Nota: {maior}.')

'''
A lógica para calcular a maior nota, com esse método (acima), é a seguinte: cada vez que o "loop" for reiniciado, a variável "nota" será substituída pela nova nota inserida pelo usuário, de modo que a última nota (inserida pelo usuário) será a nota submetida à última repetição do teste lógico que irá salvar a maior nota na variável "maior". De acordo com o que acaba de ser dito, a última nota será a única nota submetida ao teste lógico e armazenada na variável "maior" ao fim do algoritmo independentemente de ser a maior nota ou não. Para evitar esse "erro", é preciso criar uma segunda condição que irá substituir a nova nota digitada pelo usuário, ao início de cada novo "loop", pela nota que estava armazenada na variável "maior" - caso a nova nota digitada pelo usuário seja maior do que a nota que está previamente salva em "maior". Caso o novo valor não seja maior do que o previamente salvo na variável "maior", o valor de "maior" será mantido.
'''
