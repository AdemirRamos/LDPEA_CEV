#Exercícios resolvidos (Aula 06):

#1ª: Quantos anos você tem?;

nascimento = int(input('Digite o ano do seu nascimento: '))
ano = 2022
print(f'A sua idade é: {ano - nascimento}.')

#2ª: Conversão de Moeda;

valor = float(input('Digite o valor que você deseja converter: R$'))
cotação = 5. #18/01/2022
conversão = valor / cotação
print(f'A conversão do valor digitado de reais para dólares é igual a: US${conversão:.2f}.')

#3ª: Conversão de Temperatura;

temperature = float(input('Digite a temperatura em ºF: '))
fórmula = (temperature - 32) * 5 / 9
print(f'A temperatura em ºC é igual a: {fórmula:.2f}.')

#4ª: Porcentagem;

valor = float(input('Digite o valor das compras: '))
cálculo = valor * 60 / 100
print(f'O total de imposto a ser pago é: R${cálculo:.2f}.')

#5ª: Empréstimo.

valor = float(input('Digite o valor: R$'))
parcelas = int(input('Digite o número de parcelas: '))
cálculo = (valor * 20) / 100
resultado = cálculo + valor
resultado_final = resultado / parcelas
print(f'O valor das suas parcelas será de: R${resultado_final:.2f}.')
