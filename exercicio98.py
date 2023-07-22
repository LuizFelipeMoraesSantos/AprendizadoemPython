from time import sleep
def linha():
    print('-=-'*30)
def contagem(inicio,fim,passo):
    for cont in range(inicio, fim, passo):
        print(cont, end=" ")
        sleep(0.5)
    print('FIM')
def contagem_regressiva(inicio,fim, passo):
    for cont in range(inicio, fim):
        print(cont, end=" ")
        sleep(0.5)
    print('FIM')
print('Contagem de 1 até 10 de 1 em 1.')
print(f'{contagem(1, 11, 1)}')
linha()
print('Contagem de 10 até 0 de 2 em 2.')
print(f'{contagem(10, -1,-2)}')
linha()
i = int(input('Digite o primeiro número da contagem: '))
f = int(input('Digite o ultimo número da contagem: '))
c = int(input('Passo vai ser de quanto? '))
if c == 0:
    c = -1
if i > f:
    c *= -1
else:
    c *= 1
print(f'Contagem de {i} até {f} de {c} em {c}.')
print(contagem(i, f+1, c))
print('FIM')
