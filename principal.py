import funciones_aritmeticas

opcion = 1

while(opcion != 0):
    print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
    print("Escoja la operacion que desea realizar: ")
    print("1.Sumar\n2.Restar\n3.Multiplicar\n4.Dividir\n0.Salir")
    opcion = int(input())
    print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")

    if(opcion == 1):#Se realizará una suma
        numero1 = int(input("Ingrese el primer valor: "))
        numero2 = int(input("Ingrese el segundo valor: "))
        resultado = funciones_aritmeticas.sumar(numero1,numero2)
        print(f'El resultado es: {resultado}')
    elif(opcion == 2):
        numero1 = int(input("Ingrese el primer valor: "))
        numero2 = int(input("Ingrese el segundo valor: "))
        resultado = funciones_aritmeticas.restar(numero1,numero2)
        print(f'El resultado es: {resultado}')




