print("Verificador de puertos")
print("Escribe 'salir' para terminar.\n")

while True:
    entrada = input("Ingrese el número de puerto: ")

    if entrada.lower() == "salir":
        print("Saliendo del programa.")
        break

    try:
        puerto = int(entrada)

        if 0 <= puerto <= 1023:
            print("Puerto bien conocido (0 – 1023)\n")
        elif 1024 <= puerto <= 49151:
            print("Puerto registrado (1024 – 49151)\n")
        elif 49152 <= puerto <= 65535:
            print("Puerto dinámico o privado (49152 – 65535)\n")
        else:
            print("El número ingresado no corresponde a un puerto válido.\n")
    except ValueError:
        print("Entrada inválida. Debe ingresar un número entero o 'salir'.\n")