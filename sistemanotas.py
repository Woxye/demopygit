notas1 = []
notas2 = []
notas3 = []
frequencia = []
media = []
mediaG = []
menor = 0
aluno = 0
frequenciaC = 0
frequenciaG = []

def CalcMediaPond(notas1,notas2,notas3):
    valor_return = ((notas1[i]*3)+(notas2[i]*3) + (notas3[i]*4))/10
    return(valor_return)

nomedisciplina = str(input("Informe o nome da disciplina: "))
cod = int(input("Informe o código da turma: "))
quant = int(input("Informe a quantidade de alunos: "))
for i in range(quant):
    nota1 = (float(input("Informe a primeira nota do aluno: ")))
    nota2 = (float(input("Informe a segunda nota do aluno: ")))
    nota3 = (float(input("Informe a terceira nota do aluno: ")))
    frequencia = (int(input("Informe a porcentagem de frequencia do aluno: ")))
    notas1.append(nota1)
    notas2.append(nota2)
    notas3.append(nota3)
    frequenciaG.append(frequencia)
    media = CalcMediaPond(notas1,notas2,notas3)
    mediaG.append(media)
    if frequenciaG[i] < 75:
        frequenciaC += 1
    if mediaG[i] > 6 and frequenciaG[i] >= 75:
        aluno += 1
    if mediaG[i] > menor:
        menor = mediaG[i]
print("As notas finais de cada aluno foram:",mediaG)
print(f'A maior média da turma foi:[{menor}]')
print("O total de alunos aprovados foram:",aluno)
print("O total de alunos reprovados por faltas foram:",frequenciaC)





