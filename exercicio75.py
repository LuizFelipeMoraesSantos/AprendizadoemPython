n = ()
c9 = 0
posicao = 0
valores = 0
for c in range(1, 5):
    num = int(input('Digite o valor: '))
    n += (num,)
    if num == 9:
        c9 += 1
    if num == 3:
        posicao = c
    if num % 2 == 0:
        par
print(f'Os numeros digitados foram {n}')
print(f'O valor 3 foi digitado na {posicao}º posição.')
print(f'O valor 9 foi digitado {c9} vez')
print(f'O números pares foram {par}')

