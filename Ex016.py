# crie um programa que leia um numero real qualquer pelo teclado e mostre na tela a sua porção
# inteira.
# exemplo: Digite um número: 6.127. O número 6.127 tem a parte inteira 6.
from math import trunc
n = float(input('Digite um valor: '))
print('O valor digitado é {} e sua porção inteira é {}'.format(n, trunc(n)))

#caso importar da biblioteca math "import math", importará todas as funções desta biblioteca.
#daí em .format(n, math.trunc(n)).
#também tem a opção de nao importar e usar a formula interna.
#depois de .format(n, int(n)). nestes exemplos o "n" está representando a variável