'''num = somador = contador = 0
(int(input('Digite um número: ')))
while num != 999:
    somador += num
    contador += 1
    num = (int(input('Digite um número: ')))
print(f'Você digitou {contador} e a soma foi {somador}')'''
soma = contador = num = 0
while True:
    num = int(input('Qual quer número: '))
    if num == 999:
        break
    soma += num
    contador += 1
print(f'O total de numeros foi {contador}, a soma entre eles foi {soma}.')
print('Obrigado! Fim do programa')
