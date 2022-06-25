# Faça um algoritimo que leia o preço de um produto e mostre seu novo preço,
# com 5% de desconto.
p = float(input('Preço do produto: R$ '))
d = p-(5*p/100)
print('O produto que custa R$ {:.2f}\nNa promoção com desconto de 5% vai custar: R$ {:.2f}'.format(p, d), end='')
