# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e quantidade de dias pelos quais
# ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por Km rodado.

km = float(input('Quantos Km foi percorrido? Km '))
dias = int(input('Quantos dias o carro foi alugado? Dias '))
soma = (km * 0.15) + (dias * 60)
print('Você alugou um carro por {} dias e rodou {} km\nVocê irá pagar pelo aluguel um total de: R$ {:.2f}'.format(dias, km, soma), end=' ')
