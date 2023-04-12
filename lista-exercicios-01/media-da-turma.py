'''
Calcula a média da turma
Calcula a média do aluno

02 notas por aluno
'''

average_students = []
average_class = 0

for step in range(3):
    name = input(f"Digite o nome do aluno: ")
    note1 = float(input("Digite a primeira nota: "))
    note2 = float(input("Digite a segunda nota: "))

    average_student = (note1 + note2) / 2

    is_approved = "Aprovado" if average_student >= 6 else "Reprovado"

    average_students.append([name, average_student, is_approved])

for aluno in average_students:
    average_class += aluno[1] / 3

for aluno in average_students:
    print(aluno)

print(f"A média da turma é: {average_class}")
