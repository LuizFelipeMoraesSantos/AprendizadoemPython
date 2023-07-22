palavra = ('Maça', 'Abacate', 'Banana', 'Melancia', 'Abacaxi', 'Melão', 'Uva')
for p in palavra:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra in 'aeiou':
            print(letra.lower(),end=' ')


