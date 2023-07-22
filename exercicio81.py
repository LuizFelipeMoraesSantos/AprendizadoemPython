num = list()

while True:
    num.append(input('Digite um valor: '))
    escolha = str(input('Deseja continuar [S/N]:')).upper().split()[0]
    if escolha in 'Nn':
        print('Progama encerrado.')
        break
    #if escolha in 'Ss':
     #   num.append(input('Digite um valor: '))
print(f'Você digitou {len(num)} valores.')
num.sort(reverse=True)
print(f'Os números de trás pra frente ficaram {num}')
if 5 in num:
    print('O valor 5 está na lista.')
else:
    print('Nem um valor com numeral 5 está na lista.')
