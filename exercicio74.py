from random import randint
tupla = (randint(1, 10), randint(1, 10), randint(1, 10)
         , randint(1, 10), randint(1, 10))
print('As tuplas formas: ')
for cont in tupla:
    print(f'{cont}...',end='')
print(f'\nO maior numero foi {max(tupla)}')
print(f'O menor numero foi {min(tupla)}')

