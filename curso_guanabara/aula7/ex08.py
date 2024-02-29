# EX 08

def conv_medidas():
    metros_entr = float(input('Insira uma medida em METROS: '))
    return 'O valor de {}m em CENTÍMETROS é {:.2f} e em MILÍMETROS é {:.2f}'.format(
        metros_entr, metros_entr*100, metros_entr*1000
    )

print(conv_medidas())