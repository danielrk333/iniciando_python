# Conversão de Temperatura

def fahrenheit():
    celsius = float(input('Digite uma temperatura: '))
    conv_fahrenheit = (celsius * 9 / 5) + 32
    return 'A temperatura de {:.2f}°C em Fahrenheit é de {:.2f}°F'.format(
        celsius, conv_fahrenheit)


print(fahrenheit())

