'''cont = 0
num = 1
total = 0
num = int(input('Quer ver a tabuada de que valor: '))
while num > -1:
    print(f'{num} x ',end='')
    cont += 1
    print(f' {cont} = ',end='')
    total = cont * num
    print(f'{total}')
    num = int(input('Quer ver a tabuada de que valor: '))'''
num = c = 0
while True:
    num = int(input('Qual o número você quer ver a tabuada: '))
    print('-'*30)
    if num < 0:
        break
    for c in range(1,11):
        print(f'{num} x {c} = {num * c}')
    print('-' * 30)
print('PROGRAMA ENCERRADO! volte sempre.')
