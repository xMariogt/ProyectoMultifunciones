import funciones_aritmeticas

print("Escoja la operacion que desea realizar: ")
print("1.Sumar\n2.Restar\n3.Multiplicar\n4.Dividir\n0.Salir")
opcion = int(input())

if(opcion == 1):
    numero1 = int(input("Ingrese el primer valor: "))
    numero2 = int(input("Ingrese el segundo valor: "))
    resultado = funciones_aritmeticas.sumar(numero1,numero2)
    print(resultado)
