def palindromo(frase):
    tam = len(frase)
    fraseInv = ''
    for i in range(tam):
        fraseInv += frase[tam - 1 - i]

    return fraseInv

frase = input('Escreva uma frase: ')
frase = frase.lower()
frase = frase.replace(' ', '')
fraseInv = palindromo(frase)

if fraseInv == frase:
    print('A frase é um palíndromo')
else:
    print('A frase não é um palíndromo')









