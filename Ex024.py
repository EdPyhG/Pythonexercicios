#'Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".'
c = str(input('Qual cidade você nasceu? ')).strip()
print(c[:5].upper() == 'SANTO')