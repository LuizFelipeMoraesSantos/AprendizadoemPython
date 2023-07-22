primeira = float(input('Primeira nota:'))
segunda = float(input('Segunda nota: '))
media = (primeira + segunda) / 2
if media < 5:
    print(f'Sua nota foi {media}')
    print('REPROVADO')

if media >= 5 and media <= 6.9:
    print(f'Sua nota foi {media}')
    print('RECUPERAÇÃO')
elif media >= 7 and media <= 10:
    print(f'Sua nota foi {media}')
    print('APROVADO')
