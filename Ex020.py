# o mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalho dos alunos.
# Faça um progarama que leia o nome dos alunos e mostre a oredem sorteada
from random import shuffle

n1 = str(input('Aluno: '))
n2 = str(input('Aluno: '))
n3 = str(input('Aluno: '))
n4 = str(input('Aluno: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem de apresentação será: {}'.format(lista))
