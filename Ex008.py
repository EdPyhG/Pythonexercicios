# Escreva um programa que leia um valor em metros e o exiba em centímetros e milímitros
m = int(input('Digite o metro: '))
c = m * 100
mi = m * 1000
print('Este valor tem {} cm \n Este valor tem {} mm'.format(c, mi), end='')
