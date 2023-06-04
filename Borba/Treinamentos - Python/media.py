soma = 0
QtdNum = 0
maximo = float('-inf')
minimo = float('inf')

while 1:
    numero = int(input('Digite um número: '))
    soma += numero
    QtdNum += 1

    if numero > maximo:
        maximo = numero

    if numero < minimo:
        minimo = numero

    while 1:
        opção = input('Deseja digitar outro número? Responda "sim" ou "nao" ')

        if opção != 'sim' and opção != 'nao':
            continue

        else:
            break

    if opção == 'sim':
        continue

    elif opção == 'nao':
        break


media = soma/QtdNum
print('A media dos valores digitados é ', media)
print(f'O menor valor é {minimo} e o maior é {maximo}')