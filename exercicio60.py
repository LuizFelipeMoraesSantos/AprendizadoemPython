num = int(input('Fatorial: '))
cont = num + 1
soma = 1
print(f'Fatorial: {num}! = ', end='')
while cont > 1:
    cont -= 1
    soma = soma * cont
    print(f'{cont}', end='')
    print(' x ' if cont > 1 else ' = ',end='')
print(f'{soma}')






'''n = int(input('Calcule seu fatorial: '))
c = n
fat = 1
print('{}! = '.format(n),end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    fat *= c
    c -= 1
print('{}'.format(fat))'''


'''from math import factorial
n1 = int(input('Calcular seu fatorial: '))
c = factorial(n1)
print('O fatorial de {} é {}'.format(n1, c))'''







    
