import math

def ang_trig():
    ang = int(input('Insira um ângulo: '))
    rad_convert = math.radians(ang)  # tem q converter em radiano antes de usar usar o math.sin .cos ou .tan
    return 'O ângulo de {}° tem como: \n SENO: {:.2f} \n COSSENO: {:.2f} \n TANGENTE: {:.2f}'.format(
        ang, math.sin(rad_convert), math.cos(rad_convert), math.tan(rad_convert)
    )


print(ang_trig())