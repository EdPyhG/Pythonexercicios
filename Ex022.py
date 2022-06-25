#'''Crie um programa que leia o nome completo de uma pessoa e mostre:
# 01 o nome com todas as letras maiúsculas
# 02 o nome com todas as letras minúsculas
# 03 quantas letras ao todo (sem considerar espaços)
#  04 quantas letras tem o primeiro nome'''
n = str(input('Digite seu nome completo: ')).strip()
print('Seu nome em letras maiúsculas é: {}'.format(n.upper()))
print('Seu nome em letras minúsculas é: {}'.format(n.lower()))
print('Seu nome tem ao todo {} letras'.format(len(n) - n.count(' ')))
separa = n.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))
