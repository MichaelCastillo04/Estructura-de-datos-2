import sqlite3
DATOS = "diccionario.db"

#Michael Castillo 8-963-1499
#Programacion 4

def Base_datos():
    return sqlite3.connect(DATOS)


def informacion():
    tablas = []
    captar = Base_datos()
    cursor = captar.cursor()
    for tabla in tablas:
        cursor.execute(tabla)


def Menu_principal():
    informacion()

    print("\n***Dicionario de palabras de slang panameño***")
    menu = """
a) Agregar nueva palabra
b) Editar palabras
c) Eliminar palabras
d) Ver listado de palabras
e) saber significado de palabra
f) Salir
Elige: """
    eleccion = ""
    while eleccion != "f":
        eleccion = input(menu)
        if eleccion == "a":
            palabra = input("\nIngres la palabra: ")
            agregar_palabra = buscar_significado_palabra(palabra)
            if agregar_palabra:
                print(f"La palabra '{palabra}' ya existe")
            else:
                significado = input("\nIngresa el significado: ")
                agregar(palabra, significado)
                print("Palabra agregada")

        if eleccion == "b":
            palabra = input("\nIngresa la palabra a editar: ")
            nuevo_significado = input("\nIngresa el nuevo significado: ")
            editar(palabra, nuevo_significado)
            print("Palabra actualizada")

        if eleccion == "c":
            palabra = input("\nIngresa la palabra que desea eliminar: ")
            eliminar(palabra)

        if eleccion == "d":
            palabras = obtener_palabras()
            print("\n**** Lista de palabras ****")
            for palabra in palabras:
                print(palabra[0])

        if eleccion == "e":
            palabra = input("\nIngresa la palabra que desea saber su significado: ")
            significado = buscar_significado_palabra(palabra)
            if significado:
                print(f"\nEl significado de '{palabra}' es: {significado[0]}")
            else:
                print(f"Palabra '{palabra}' no encontrada")


def agregar(palabra, significado):
    conexion = Base_datos()
    cursor = conexion.cursor()
    sentencia = "INSERT INTO diccionario(palabra, significado) VALUES (?, ?)"
    cursor.execute(sentencia, [palabra, significado])
    conexion.commit()


def editar(palabra, nuevo_significado):
    conexion = Base_datos()
    cursor = conexion.cursor()
    sentencia = "UPDATE diccionario SET significado = ? WHERE palabra = ?"
    cursor.execute(sentencia, [nuevo_significado, palabra])
    conexion.commit()


def eliminar(palabra):
    conexion = Base_datos()
    cursor = conexion.cursor()
    sentencia = "DELETE FROM diccionario WHERE palabra = ?"
    cursor.execute(sentencia, [palabra])
    conexion.commit()


def obtener_palabras():
    conexion = Base_datos()
    cursor = conexion.cursor()
    consulta = "SELECT palabra FROM diccionario"
    cursor.execute(consulta)
    return cursor.fetchall()


def buscar_significado_palabra(palabra):
    conexion = Base_datos()
    cursor = conexion.cursor()
    consulta = "SELECT significado FROM diccionario WHERE palabra = ?"
    cursor.execute(consulta, [palabra])
    return cursor.fetchone()


if __name__ == '__main__':
    Menu_principal()