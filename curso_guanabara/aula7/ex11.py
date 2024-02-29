# EX 11

def qtd_tinta():
    alt = float(input('Insira a ALTURA da parede em METROS: '))
    larg = float(input('Insira a LARGURA da parede em METROS: '))
    area = alt * larg
    print()
    print('Sua parede tem a área de {}m2!'.format(area))
    return 'Você precisará de {}L de tinta!'.format(area / 2)


print(qtd_tinta())
