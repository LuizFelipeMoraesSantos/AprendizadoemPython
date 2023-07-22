print('Gerenciamento de uma P.A')
print('-='*20)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da P.A: '))
cont = 0
termos = 0
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(termo),end='')
        termo += razao
        cont += 1
print('PAUSA')
mais = int(input('Qauntos termos você quer a mais: '))




