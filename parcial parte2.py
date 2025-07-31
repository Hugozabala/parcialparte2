def menu():
    print(" =====menu principal")
    print("1. Calcular el MCD de dos numeros (recursivos")
    print("2. crear un cadena repetida n veces")
    print("3. contar cuantas veces aparece una letra en una cadena ")
    print("4. convertir un numero decimal a vinario")
    print("5. calcular cuantos digitos tiene un numero")
    print("6. salir")

def cadena_rep3(cadena):
    if len(cadena)==0:
        return 0
    else:
        return cadena +cadena +cadena

def cadena_letra_repetida(cadena1):
    if len(cadena1)==0:
        return 0
    else:
        return

def suma_digitos(n):
    if n < 10:
        return n
    else:
        return n % 10 + suma_digitos(n // 10)

def mcd_de_numero(num,num2):
    if ((num <=0 )or(num2 <=0)) :
        return 0
    else:

        return(num1 or num2)/mcd_de_numero(num1-1)




op=0
while op!=6:
    menu()
    op=int(input("ingrese opcion a ejecutar"))
    match (op):
        case 1:
            num1 =int(input("ingrese primer numero"))
            num2= int(input("ingrse segundo numero"))

        case 2:
            cad=input("ingrese palabra")
            cadena_rep3(cad)
            print(cadena_rep3(cad))


        case 3:
            cad1=input("ingrese una palabra")

        case 4:
            num2=int(input("ingrse un numero para convertirlo a binario"))


        case 5:
            num3=int(input("ingrse un numero entero"))
            suma_digitos(num3)
            print(suma_digitos(num3))
            break

        case 6:
            print("fin de programa")

        case _:
            print("ingrese una opcion correcta")













