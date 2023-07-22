colegio = []
aluno = {}

aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input('Média: '))
if aluno['media'] <= 5.9:
    aluno['situação'] = 'Reprovado'
elif aluno['media'] >= 6:
    aluno['situação'] = 'Aprovado'
colegio = aluno.copy()
print(f"O Nome do aluno é {colegio['nome']}!")
print(f"A média é {colegio['media']}.")
print(f'Situaçao: {colegio["situação"]}')



