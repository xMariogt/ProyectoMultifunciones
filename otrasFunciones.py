import funciones_aritmeticas as aritmeticas

def Permutacion(N, r):
    resultado = aritmeticas.factorial(N)/aritmeticas.factorial(N-r)
    print(f'El resultado de la permutacion es: {resultado}')
    return resultado

def Combinacion(N,r):
    resultado = aritmeticas.factorial(N)/(aritmeticas.factorial(N-r)*aritmeticas.factorial(r))
    print(f'El resultado de la combinacion es: {resultado}')
    return resultado