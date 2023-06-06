lista = []

while 1:
    dicionario = {}
    nome = input("Digite o nome do jogador: ")
    dicionario.update({'Nome': nome})

    partidas = int(input("Quantas partidas ele jogou? "))
    soma = 0
    for i in range(partidas):
        gols = int(input(f'Quantos gols o jogador fez na partida {i+1}? '))
        dicionario.update({'Gols na partida {}'.format(i+1) : gols})
        soma += gols

    dicionario.update({'Total de gols' : soma})

    lista.append(dicionario)

    while 1:
        opcao = input('Você deseja cadastrar mais um jogador? Responda "sim" ou "nao":  ')

        if opcao != 'sim' and opcao != 'nao':
            print('Reposta inválida')
            continue

        else:
            break

    if opcao == 'nao':
        break

    if opcao == 'sim':
        continue

tamLista = len(lista)
soma = 0
for dicionario in lista:
    gols = dicionario.get('Total de gols', 0)
    soma +=gols

for x in lista:
    print(x)

print(f'O total de gols marcados pelo time foi {soma}')



