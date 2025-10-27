# 🗂️ Proyecto 2: Gestor de Archivos en Consola

## 📘 Descripción
Aplicación de consola en **Python** que permite gestionar archivos y carpetas del sistema de manera sencilla.  
El usuario puede **listar contenido**, **crear y eliminar directorios o archivos**, **escribir dentro de ellos** y **consultar información básica** (tamaño, fecha de modificación, tipo).

Este proyecto forma parte del módulo de **Programación en Python**, donde se aplican estructuras de control, manejo de archivos y el módulo `os`.

---

## 🚀 Funcionalidades Principales

### Menú principal
El programa muestra continuamente un menú con las siguientes opciones:

1. Listar contenido del directorio actual  
2. Crear un nuevo directorio  
3. Crear un archivo de texto  
4. Escribir texto en un archivo existente  
5. Eliminar un archivo o directorio  
6. Mostrar información del archivo  
7. Salir

---

## ⚙️ Requisitos del Sistema
- Python 3.8 o superior  
- Sistema operativo compatible con `os` (Windows, macOS o Linux)

---

## 🧠 Contenidos del módulo aplicados
- Entrada y salida por consola  
- Manejo de archivos (`open`, `read`, `write`, `append`)  
- Uso del módulo `os`  
- Control de flujo (`if`, `elif`, `else`)  
- Bucles (`while`, `for`)  
- Funciones con parámetros y retorno  
- Manejo de excepciones (`try`, `except`)

---

## 🧩 Estructura del Programa

```python
def mostrar_menu():            # Muestra las opciones disponibles
def listar_contenido():        # Lista archivos y carpetas del directorio actual
def crear_directorio():        # Crea una nueva carpeta
def crear_archivo():           # Crea un archivo de texto y permite escribir contenido inicial
def escribir_en_archivo():     # Añade texto a un archivo existente
def eliminar_elemento():       # Elimina un archivo o carpeta
def mostrar_informacion():     # Muestra tamaño y fecha de modificación
def main():                    # Bucle principal del programa
