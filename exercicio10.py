'''Uma escola deseja armazenar as notas de 3 alunos em 4 bimestres.
Utilize uma matriz para armazenar as notas e exiba:
Todas as notas
Média de cada aluno
Situação (Aprovado ou Reprovado)
Considere média mínima 7.'''


notas = []

for aluno in range(3):
    notas_aluno = []
    print(f"\nAluno {aluno + 1}")

    for bimestre in range(4):
        nota = float(input(f"Digite a nota do {bimestre + 1}º bimestre: "))
        notas_aluno.append(nota)

    notas.append(notas_aluno)

print("\n Situação dos Alunos")

for aluno in range(3):
    media = sum(notas[aluno]) / 4

    if media >= 7:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"

    print(f"\nAluno {aluno + 1}")
    print(f"Notas: {notas[aluno]}")
    print(f"Media: {media:.2f}")
    print(f"Situacao: {situacao}")