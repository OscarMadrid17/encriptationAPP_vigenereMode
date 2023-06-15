def encriptar_vigenere(mensaje, clave):
    mensaje = mensaje.upper()
    clave = clave.upper()
    mensaje_encriptado = ""

    for i in range(len(mensaje)):
        if mensaje[i].isalpha():
            letra_mensaje = ord(mensaje[i]) - 65
            letra_clave = ord(clave[i % len(clave)]) - 65
            letra_encriptada = (letra_mensaje + letra_clave) % 26 + 65
            mensaje_encriptado += chr(letra_encriptada)
        else:
            mensaje_encriptado += mensaje[i]

    return mensaje_encriptado


def encriptar_archivo(ruta_archivo, clave):
    try:
        with open(ruta_archivo, 'r') as archivo_original:
            contenido = archivo_original.read()
            contenido_encriptado = encriptar_vigenere(contenido, clave)

            nombre_archivo_salida = ruta_archivo[:-4] + 'C.txt'

            with open(nombre_archivo_salida, 'w') as archivo_encriptado:
                archivo_encriptado.write(contenido_encriptado)

            print("Archivo encriptado guardado como:", nombre_archivo_salida)

    except FileNotFoundError:
        print("El archivo no existe.")
    except Exception as e:
        print("Se produjo un error al encriptar el archivo:", str(e))


# Solicitar la ruta del archivo y la clave al usuario
ruta_archivo = input("Ingrese la ruta del archivo de texto a encriptar: ")
clave = input("Ingrese la clave de encriptación: ")

# Encriptar el archivo
encriptar_archivo(ruta_archivo, clave)
