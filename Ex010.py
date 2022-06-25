# Crie um programa que mostre quanto $$ ela tem na carteira e mostre quantos dólares ela pode comprar
# Considerando USD 1,00 = R$ 3,27
r = float(input('Quanto você tem na carteira? R$ '))
print('Com R$ {:.2f} você pode comprar USD: {:.2f}'.format(r, r/3.27))
