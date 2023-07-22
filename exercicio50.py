soma = 0
cont = 0
for c in range(1, 7):
    num = int(input(f'DIGITE UM VALOR {c}: '))
    if num % 2 == 0:
        cont = cont + 1
        soma = soma + num
print(f'Você digitou {cont} números pares e a soma entre eles foi {soma}')