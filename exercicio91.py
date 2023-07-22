from random import randint
from time import sleep
from  operator import itemgetter
biblioteca = {'jogador1': randint(1, 6),
              'jogador2': randint(1, 6),
              'jogador3': randint(1, 6),
              'jogador4': randint(1, 6)}
print('\033[32mVALORES SORTEADOS\033[m.')
rankig = {}
for k, v in biblioteca.items():
    print(f'O {k} tirou {v} no dado.')
    sleep(1)
rankig = sorted(biblioteca.items(), key=itemgetter(1), reverse=True)
print('\033[32mRANKING DOS JOGADORES\033[m.')
for i, v in enumerate(rankig):
    print(f'O {i + 1}º no lugar: {v[0]} com {v[1]}.')
    sleep(1)