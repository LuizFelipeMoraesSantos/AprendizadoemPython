cont1000 = caro = barato = menor = cont = somatotal  = 0
while True:
    nome = str(input('NOME DO PRODUTO: ')).upper()
    preco = float(input('VALOR R$: '))
    stop = str(input('Quer continuar[S/N]: ')).upper().strip()[0]
    somatotal += preco
    cont += 1
    if stop == 'N':
        break
    if cont == 1:
        menor = preco
    else:
        if preco < menor:
            menor = preco
print(f'Total foi iqual R$ {somatotal}')
print(f'A quantidade de valores acima de R$ 1000.00 foi de {cont1000} unidades')
print(f'O produto mais barato foi {menorpreco}')







