import json

try:
    
    with open('dispositivos.json', 'r') as archivo:
        datos = json.load(archivo)

    dispositivos_data = datos.get("dispositivos", [])

    print("\n Lista de dispositivos:\n")

    for dispositivo in dispositivos_data:
        nombre = dispositivo.get("nombre", "Desconocido")
        ip = dispositivo.get("ip", "No especificada")
        estado = dispositivo.get("estado", "Desconocido")

        print(f"Nombre : {nombre}")
        print(f"   IP     : {ip}")
        print(f"   Estado : {estado}\n")

except FileNotFoundError:
    print("El archivo 'dispositivos.json' no fue encontrado.")
except json.JSONDecodeError:
    print("Error al decodificar el archivo JSON.")