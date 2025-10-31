import os
from datetime import datetime

def mostrar_menu():

    # Muestra la ruta actual del directorio
    print(f"\nRuta actual: {os.getcwd()}")

    #Menú principal
    print("\n### MENÚ ###")
    print("\n1. Listar contenido del directorio actual")
    print("\n2. Crear un nuevo directorio")
    print("\n3. Crear un archivo de texto")
    print("\n4. Escribir texto en un archivo existente")
    print("\n5. Eliminar un archivo o directorio")
    print("\n6. Mostrar información del archivo")
    print("\n7. Salir")




def listar_contenido():


    print(f"\nRuta actual: {os.getcwd()}")
    # Lista archivos y carpetas del directorio actual
    try:
        ruta_actual = os.getcwd()
        elementos = os.listdir(ruta_actual)

        if len(elementos) == 0:
            print("El directorio está vacío.")
        else:
            print("\n### Carpetas y archivos ###")
            for elemento in elementos:
                ruta_elemento = os.path.join(ruta_actual, elemento)

                if os.path.isdir(ruta_elemento):
                    print(f"[DIR] {elemento}")
                elif os.path.isfile(ruta_elemento):
                    print(f"[FILE] {elemento}")
                else:
                    print(f"[OTRO] {elemento}")
    except Exception as e:
        print(e)



def crear_directorio():

    print(f"\nRuta actual: {os.getcwd()}")

    print()
    # Crea una nueva carpeta
    nombre_directorio = input("\nEscribe el nombre para el nuevo directorio: ").strip()

    if not nombre_directorio:
        print("\nEl nombre no puede estar vacío.")
        return

    try:
        ruta_destino = os.path.join(os.getcwd(), nombre_directorio)

        if os.path.exists(ruta_destino):
            print("Ya existe ese directorio")
            return
        else:
            os.mkdir(ruta_destino)
            print(f"Directorio '{nombre_directorio}' creado correctamente.")
    except Exception as e:
        print(f"Error al crear el directorio: {e}")



def crear_archivo():
    print(f"\nRuta actual: {os.getcwd()}")
    nombre_archivo = input("Introduce el nombre que deseas poner al archivo nuevo: ").strip()

    if not nombre_archivo:
        print("El nombre del archivo no puede estar vacío.")
        return

    try:
        with open(nombre_archivo, 'x') as file:
            anadir_texto_inicial = input("¿Deseas añadir texto inicial? (si/no): ").strip().lower()

            if anadir_texto_inicial == "si":
                texto_inicial = input("Escribe el texto que quieras añadir al archivo: ")
                file.write(texto_inicial)
                print(f"Se ha guardado el texto en {nombre_archivo} correctamente.")
            elif anadir_texto_inicial == "no":
                print(f"Has creado el archivo {nombre_archivo} vacío correctamente.")
            else:
                print(f"Opción no válida. Se ha creado el archivo {nombre_archivo} vacío.")
    except FileExistsError:
        print(f"Ya existe un archivo llamado '{nombre_archivo}'.")
    except Exception as e:
        print(f"Error al crear el archivo {nombre_archivo}: {e}")




def escribir_en_archivo():
    # Muestra la ruta actual del directorio
    print(f"\nRuta actual: {os.getcwd()}")

    archivo_anadir_texto = input("Introduce el nombre del archivo que quieres añadir texto: ")

    if not archivo_anadir_texto:
        print("El nombre no puede estar vacío.")
        return

    try:
        with open(archivo_anadir_texto, 'a') as file:
            texto_a_anadir = input("Escribe el texto que deseas añadir al archivo: ")

            if not texto_a_anadir.strip():
                print("No se ha añadido ningún texto porque estaba vacío.")
                return
            file.write("\n" + texto_a_anadir)
            print(f"Texto añadido correctamente a {archivo_anadir_texto}")
    except FileNotFoundError:
        print(f"El archivo {archivo_anadir_texto} no se ha encontrado en el directorio.")
    except Exception as e:
        print(f"Error al escribir en el archivo {archivo_anadir_texto}: {e}")

def eliminar_elemento():
    # Muestra la ruta actual
    print(f"\nRuta actual: {os.getcwd()}")

    nombre_elemento_borrar = input("Escribe el nombre del elemento que deseas eliminar: ").strip()

    if not nombre_elemento_borrar:
        print("El nombre del elemento a eliminar no puede estar vacío.")
        return

    try:
        if os.path.exists(nombre_elemento_borrar):
            if os.path.isfile(nombre_elemento_borrar):
                os.remove(nombre_elemento_borrar)
                print(f"Has eliminado el archivo {nombre_elemento_borrar} correctamente.")
            elif os.path.isdir(nombre_elemento_borrar):
                os.rmdir(nombre_elemento_borrar)
                print(f"Has eliminado el directorio {nombre_elemento_borrar} correctamente.")
            else:
                print(f"El elemento {nombre_elemento_borrar} no existe en el directorio actual.")
    except PermissionError:
        print(f"No tienes los suficientes permisos para eliminar {nombre_elemento_borrar}.")
    except FileNotFoundError:
        print(f"El archivo {nombre_elemento_borrar} no existe en el directorio.")
    except IsADirectoryError:
        print(f"El directorio {nombre_elemento_borrar} no existe.")
    except OSError:
        print(f"El directorio {nombre_elemento_borrar} debe estar vacío para eliminarse")

def mostrar_informacion():
    # Muestra la ruta actual del directorio
    print(f"\nRuta actual: {os.getcwd()}")

    nombre_elemento_informacion = input("Introduce el nombre del elemento para mostar su información: ").strip()

    if not nombre_elemento_informacion:
        print("El nombre no puede estar vacío.")
        return

    try:
        if os.path.exists(nombre_elemento_informacion):
            fecha_modificacion = datetime.fromtimestamp(os.path.getmtime(nombre_elemento_informacion))
            print(f"\n=== Información de '{nombre_elemento_informacion}' ===")

            if os.path.isfile(nombre_elemento_informacion):
                print(f"Tamaño de {nombre_elemento_informacion}: {os.path.getsize(nombre_elemento_informacion)} bytes")
                print(f"Fecha de modificación de {nombre_elemento_informacion}: {fecha_modificacion}")
            elif os.path.isdir(nombre_elemento_informacion):
                tam = calcular_tamanio_directorio(nombre_elemento_informacion)
                print(f"Tamaño del directorio: {tam} bytes.")
                print(f"Fecha de modificación de {nombre_elemento_informacion}: {fecha_modificacion}")
            else:
                return
        else:
            print("El elemento no existe en el directorio actual.")
    except Exception as e:
        print(e)


def calcular_tamanio_directorio(ruta_dir):
    total_bytes = 0
    for raiz, subdirs, archivos in os.walk(ruta_dir):
        for nombre in archivos:
            ruta_archivos = os.path.join(raiz, nombre)
            try:
                total_bytes += os.path.getsize(ruta_archivos)
            except Exception:
                pass
    return total_bytes


def main():


    """
     Función principal del programa.
     Muestra el menú de opciones y ejecuta la acción correspondiente
     según la elección del usuario.
     """
    while True:
        mostrar_menu()

        # Pide al usuario que elija una opción
        opcion = input("Introduce una opción (1-7): ").strip()

        # Opción 1: Listar contenido del directorio actual
        if opcion == "1":
            listar_contenido()
        # Opción 2: Crear nuevo directorio
        elif opcion == "2":
            crear_directorio()
        # Opción 3: Crear archivo de texto
        elif opcion == "3":
            crear_archivo()
        # Opción 4: Escribir en un archivo existente
        elif opcion == "4":
            escribir_en_archivo()
        # Opción 5: Eliminar un archivo o directorio
        elif opcion == "5":
            eliminar_elemento()
        # Opción 6: Mostrar información del archivo
        elif opcion == "6":
            mostrar_informacion()
        # Opción 7: Salir del programa
        elif opcion == "7":
            print("Cerrando menú....")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

main()