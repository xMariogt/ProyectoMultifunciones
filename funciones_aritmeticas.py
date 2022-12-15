def sumar(numero1, numero2):
    return numero1+numero2

def restar(numero1, numero2):
    return numero1-numero2

def multiplicar(numero1, numero2):
    return numero1*numero2

def dividir(numero1, numero2):
    return numero1/numero2

def factorial(numero):
    if numero > 1:
        resultado = numero * factorial(numero - 1)
        
    elif numero == 0 or numero == 1:
        resultado = 1
    return resultado