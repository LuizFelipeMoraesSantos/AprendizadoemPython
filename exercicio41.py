from datetime import date
print('~'*30)
print('Categoria do nadador')
print('~'*30)
ano_nascimento = int(input('Data de nascimneto(****): '))
ano = date.today().year
idade = ano - ano_nascimento
print(f'Sua idade é {idade} anos')
if idade <= 9:
    print(f'Sua categoria é MIRIM')
elif idade >= 10 and idade <= 14:
    print(f'Sua categoair é INFANTIL')
elif idade >= 15 and idade <= 19:
    print(f'Sua categoria é JUNIOR')
elif idade >= 20 and idade <= 25:
    print(f'Sua categoria é SÊNIOR')
else:
    print('Sua categoria é MASTER')