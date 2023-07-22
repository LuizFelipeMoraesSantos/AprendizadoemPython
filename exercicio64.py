soma = num = contador = maior = menor = media = 0
resposta = 'S'
while resposta in 'Ss':
    num = (int(input('Digite um número: ')))
    contador += 1
    soma += num
    if contador == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resposta = str(input('Quer continuar [S/N]? ')).upper().strip()[0]
media = (soma / contador)
print('Você digitou {} números e a média foi {}'.format(contador, media))
print('O maior valor foi {} e o menor {}'.format(maior, menor))
