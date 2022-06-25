#Faça um algoritimo que leia o salário de um funcionário e mostre o seu novo salário, com 15% de aumento.
salário = float(input('Qual é o salário do funcionário? R$ '))
novo = salário + (salário * 15 / 100)
print('O funcionário que ganhava: R$ {:.2f}\nCom aumento de 15% passa a ganhar um novo salário de: R$ {:.2f}'.format(salário, novo), end=' ')
