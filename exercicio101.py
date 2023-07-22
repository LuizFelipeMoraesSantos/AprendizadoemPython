def voto(i):
    global idade
    if idade >= 18 and idade < 65:
        i = ' Voto obrigatorio.'
    elif idade >= 65:
        i = ' Voto Facultativo'
    else:
        i = ' Não precisa votar'
    return i

from datetime import datetime
nasc = int(input('Em que ano você nasceu(****): '))
ano_atual = datetime.now().year
idade = ano_atual - nasc
print(f'Você tem {idade} anos: {voto(nasc)}')
