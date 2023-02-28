# Cálculo da pontuação única do System Usability Scale (SUS)

listAnswer = []
total = 0

for value in range(1,11):
    answer = int(input())
    listAnswer.append(answer)

for value in range(1,11):
    if value % 2 == 0:
        total = total + (5 - listAnswer[value-1])
    else:
        total = total + (listAnswer[value-1] - 1)

result = total*2.5

print("Resultado SUS: %f" % result)

