#'Crie um programa que leia um nome de uma pessoa e diga se ela tem 'SILVA' no nome.'
nome = str(input('Digite seu nome: ')).strip()
print('Você tem Silva no nome? = {}'.format('silva' in nome.lower()))