from datetime import date
ano = int(input('Que ano você nasceu: '))
atual = 2023
idade = atual - ano
alistamento = ano + 18
if idade < 18:
    print(f'Sua idade é {idade} anos.')
    print(f'Ainda faltam {18 - idade} anos para se alistar.')
    print(f'Você se alistara em {alistamento}.')
if idade > 18:
    print(f'Sua idade é {idade} anos.')
    print(f'Já se passou {(atual - ano - 18)} anos da data de alistamento.')
    print(f'Era para ter se alistado em {alistamento}.')
if idade == 18:
    print('Voce está em ano de alistamento.')