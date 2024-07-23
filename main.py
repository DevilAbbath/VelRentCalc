import math
import VelEscape
import RentCalc

print("********** Advertencia **********")
print("*   Este programa solo admite   *")
print("*   Numeros, favor precaucion   *")
print("*  con los valores a ingresar   *")
print("*********************************")

print("Seleccione la operacion")
print("1. Calcular Velocidad de escape")
print("2. Calcular Rentabilidad")

option = float(input("Su opcion: "))

if option == 1:
    print("\nCalcular Velocidad de escape")
    gravity = float(
        input("Ingrese Constante Gravitacional (g) en metro por segundo: "))
    pradius = float(input("Ingrese Radio del Planeta en kilometros: "))
    vescape = VelEscape.velescape(gravity, pradius)
    print("\nLa velocidad de escape del planeta es de:")
    print(f'{vescape}[m/s]\n')

elif option == 2:
    print("\nSeleccione la version")
    print("1. Utilidades Version 1 (no difiere de standar vs premium)")
    print("2. Utilidades Version 2 (incluye diferenciacion de usuarios)")
    print("3. Razon entre utilidades")
    calcoption = float(input("Su opcion: "))

    if calcoption == 1:
        print("\nUtilidades Version 1")
        print("No difiere de standar vs premium")
        csubs = float(input("Indique costo suscripcion: "))
        quser = float(input("Indique Cantidad de usuarios: "))
        texpenses = float(input("Valor de los gastos totales: "))

        utilities = RentCalc.rentcalcv1(csubs, quser, texpenses)

        print(f'\nSus utilidades actuales son de un valor de ${utilities}\n')

    elif calcoption == 2:
        print("\nUtilidades Version 2")
        print("Aplicado costo extra para usuarios premium\n")
        csubs = float(input("Indique costo suscripcion: "))
        qsuser = float(input("Indique Cantidad de usuarios Estandar: "))
        qpuser = float(input("Indique Cantidad de usuarios Premium: "))
        texpenses = float(input("Valor de los gastos totales: "))

        utilities = RentCalc.rentcalcv2(csubs, qsuser, qpuser, texpenses)

        print(f'\nSus utilidades actuales son de un valor de ${utilities}')

    elif calcoption == 3:
        print("\nRazon entre utilidades")
        print("Recordar tener valor total de las utilidades del año anterior\n")

        previousprofits = float(input("Valor utilidades del año anterior: "))
        csubs = float(input("Indique costo suscripcion: "))
        qsuser = float(input("Indique Cantidad de usuarios Estandar: "))
        qpuser = float(input("Indique Cantidad de usuarios Premium: "))
        texpenses = float(input("Valor de los gastos totales: "))

        actualprofits = RentCalc.rentcalcv2(csubs, qsuser, qpuser, texpenses)
        mathreason = RentCalc.mathreason(actualprofits, previousprofits)
        
        print (f'\nLa razon comparativa de las utilidades es de un {mathreason}%\n')

    else:
        print("\n option Invalida \n")

else:
    print("\n option Invalida \n")
