#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente
import math
angulo = float(input('Digite um ângulo: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('O ângulo de {}\ntem o SENO de {:.2f}\no COSSENA de {:.2f}\ne a TANGENTE de {:.2f}'.format(angulo, seno, cosseno, tangente))
