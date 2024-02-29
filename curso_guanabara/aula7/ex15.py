# EX 15

def preco_aluguel():
    dias = int(input('Quantos dias o veículo foi contratado? '))
    km = float(input('Quantos KM o veículo rodou? '))
    return 'O valor total é de R${:.2f}'.format((dias*60) + (km*0.15))


print(preco_aluguel())