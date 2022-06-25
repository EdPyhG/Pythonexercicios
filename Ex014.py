#Converta graus Cº em Fº
c = float(input('Informe a temperatura em ºC: '))
f = ((9*c)/5)+32
print('A temperatura de {}ºC corresponde a {}ºF'.format(c, f))
#Este exercício também poderia ser feito sem os (), porque seguindo a regra de precedência
# o '*' e o '/' tem a mesma ordem, então se lê o primeiro e o '+' tem a última ordem.
