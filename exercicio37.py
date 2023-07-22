num = int(input('Digite um número: '))
print('''Escolha:
[1] para Binário
[2] para octal
[3] para hexadecimal''')
escolha = int(input('Aperte uma das 3 opções: '))
binario = bin(num)
octal = oct(num)
hexagonal = hex(num)
if escolha == 1:
    print(f'O binario de {num} é {binario[2:]}')
if escolha == 2:
    print(f'O octal de {num} é {octal[2:]}')
if escolha == 3:
    print(f'O hexagonal de {num} é {hexagonal[2:]}')
else:
    print('Digitação invalida')

