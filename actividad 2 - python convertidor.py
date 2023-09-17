def mixkm():
    milla = int(input("Ingrese mi (milla)"))
    division = 1609/1
    km = milla * division
    print('La conversión de ', milla, ' mi a km es: ', km)

def gradoxfh():
    grado = int(input('Ingrese grados centígrados'))
    multi = 1.8*grado
    fh = multi + 32
    print('La conversión de ', grado, ' grados centígrados a Fahrenheit es: ', fh)

def binxdec():
    long = int(input('Para ingresar binario, primero porfavor determine la longitud del binario: '))
    print("Ingrese uno a uno los números de binarios de derecha a izquierda: ")
    base = 0
    decimal = 0
    totalElevado = 0
    for ciclo in range(long):
        binario = int(input('Ingrese el ' +  str(ciclo) +' binario: '))
        if binario == 1:
            decimal = (2 ** base)
            totalElevado = totalElevado + decimal
        base = base + 1
    print('La conversión de binario a decimal es: ' + str(totalElevado))

def llamar_funcion(numero):
    if numero == 1:
        mixkm()
    elif numero == 2:
        gradoxfh()
    elif numero == 3:
        binxdec()
    else:
        print("Error - No se encontró la conversión seleccionada, vuelva a correr el proceso")

# Obtener el número de entrada
try:
    print("Proceso de conversión de:")
    print("1 = mi (millas) a km (kilómetros)")
    print("2 = grados centígrados a fahrenheit")
    print("3 = binario a decimal")
    numeroConversion = int(input("Seleccione el número de conversión a continuación: "))
    llamar_funcion(numeroConversion)
except ValueError:
    print("Entrada no válida. Por favor, ingrese un número entero.")
