dias = int(input('Por quantos dias o carro foi alugado?'))
rodagem = float(input('Quantos km o carro andou?'))
preço = 60*dias + 0.15*rodagem
print('O preço a ser pago pelo aluguel é', preço)