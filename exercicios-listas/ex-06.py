'''
06 - Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.
'''

averages = []
students = []

for i in range(2):
    grades = []

    name = input(f"Digite o nome do {i+1}º aluno: ").upper()

    students.append(name)

    for i in range(4):
        grade = float(input(f"Digite a {i+1}ª nota do aluno {name}: "))
        grades.append(grade)

    averages.append(sum(grades) / len(grades))
    
    print(f"{30 * '*'}")
    
print("Alunos com média maior ou igual a 7:")
for index, average in enumerate(averages):
    if (average >= 7):
        print(f"Nome: {students[index]} | Média: {average}")
