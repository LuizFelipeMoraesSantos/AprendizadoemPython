# termos da progreção geometrica
primeiro = int(input('primeiro termo: '))
razao = int(input('Razão: '))
cont = 11
while cont > 1:
    print(f' {primeiro} -> ', end='')
    cont -= 1
    primeiro += razao
print('Fim')

'''print('gerador de P.A')
p1 = int(input('Primeiro termo: '))
r = int(input('Razao da P.A: '))
c = 0
pg = p1
while c < 10:
    print('{} -> '.format(pg), end='')
    pg = pg + r
    c = c + 1
print('Fim')'''