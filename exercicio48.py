soma = 0
cont = 0
for c in range(0, 501, 2):
    if c % 3 == 0:
        soma += c
        cont += 1
        print(c)
print(f'o total de valores foi {cont} e o total da soma é {soma} ')
