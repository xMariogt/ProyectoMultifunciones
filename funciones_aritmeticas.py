def sumar(numero1, numero2):
    resultado = numero1+numero2
    print(f'El resultado es: {resultado}')
    return resultado

def restar(numero1, numero2):
    resultado = numero1-numero2
    print(f'El resultado es: {resultado}')
    return resultado

def multiplicar(numero1, numero2):
    resultado = numero1*numero2
    print(f'El resultado es: {resultado}')
    return resultado

def dividir(numero1, numero2):
    resultado = numero1/numero2
    print(f'El resultado es: {resultado}')
    return resultado

def factorial(numero):
    if numero > 1:
        resultado = numero * factorial(numero - 1)
        
    elif numero == 0 or numero == 1:
        resultado = 1
    return resultado