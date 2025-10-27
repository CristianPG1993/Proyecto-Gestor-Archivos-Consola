import os

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
    # Crea un archivo de texto y permite escribir en él
    pass

def escribir_en_archivo():
    # Abre un archivo existente y añade texto al final
    pass

def eliminar_elemento():
    # Elimina un archivo o carpeta
    pass

def mostrar_informacion():
    # Muestra tamaño y fecha de modificación
    pass

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