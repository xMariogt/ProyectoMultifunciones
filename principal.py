import funciones_aritmeticas

opcion = 1

while(opcion != 0):
    print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
    print("Escoja la operacion que desea realizar: ")
    print("1.Sumar\n2.Restar\n3.Multiplicar\n4.Dividir\n0.Salir")
    opcion = int(input())
    print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")

    if(opcion == 1):#Funcion de suma
        numero1 = int(input("Ingrese el primer valor: "))
        numero2 = int(input("Ingrese el segundo valor: "))
        resultado = funciones_aritmeticas.sumar(numero1,numero2)
        print(f'El resultado es: {resultado}')
    elif(opcion == 2):#Funcion de resta
        numero1 = int(input("Ingrese el primer valor: "))
        numero2 = int(input("Ingrese el segundo valor: "))
        resultado = funciones_aritmeticas.restar(numero1,numero2)
        print(f'El resultado es: {resultado}')
    elif(opcion == 3):#Funcion de multiplicacion
        numero1 = int(input("Ingrese el primer valor: "))
        numero2 = int(input("Ingrese el segundo valor: "))
        resultado = funciones_aritmeticas.multiplicar(numero1,numero2)
        print(f'El resultado es: {resultado}')
    elif(opcion == 4):#Funcion de division
        numero1 = int(input("Ingrese el primer valor: "))
        numero2 = int(input("Ingrese el segundo valor: "))
        resultado = funciones_aritmeticas.dividir(numero1,numero2)
        print(f'El resultado es: {resultado}')
    elif(opcion == 5): #Funcion Factorial
        numero1 = int(input("Ingrese el valor: "))
        resultado = funciones_aritmeticas.factorial(numero1)
        print(f'El resultado es: {resultado}')




