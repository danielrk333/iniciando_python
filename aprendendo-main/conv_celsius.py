# Conversor de °C em °F

def conv():
    celsius = float(input("Insira uma temperatura em °C: "))
    fahrenheit = (celsius*9/5)+32
    return fahrenheit

print(conv())