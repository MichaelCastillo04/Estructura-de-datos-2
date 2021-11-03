import collections
from bson.py3compat import b
import pymongo

from pymongo import MongoClient

cluster = MongoClient(
    "mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000L")
db = cluster["MongoDB"]
collection = db["Diccionario"]


def VerificarPalabra(Palabra):
    verificar = collection.find_one(
        {"palabra": Palabra})
    if(verificar == None):
        return False
    else:
        return True


def Actualizar(AntiguaPalabra, NuevaPalabra, NuevaDefinicion):
    collection.update_one({"palabra": AntiguaPalabra}, {"$set": {
        "palabra": NuevaPalabra,
        "definicion": NuevaDefinicion
    }})


def Borrar(Palabra):
    collection.delete_one({"palabra": Palabra})


def Mostrar():
    palabras = collection.find()
    i = 0
    print("\n**** Lista de palabras ****\n")
    for row in palabras:
        i += 1
        print(
            f'{i}. Palabra: {row["palabra"]}')


while True:

    # Menú de opciones
    print("\n***Dicionario de palabras de slang panameño***\n")

    Opcion = int(input(" 1). Agregar nueva palabra \n 2). Editar palabra \n 3). Eliminar palabra \n 4). Ver listado de palabras \n 5). Saber significado de palabra \n 0). Salir \n"))

    if(Opcion == 1):
       # Se introduce palabra y definición
        AgregarPalabra = input("\nIngrese palabra a agregar:\n")
        Definicion = input("\nIngrese definición:\n")
        if(len(AgregarPalabra) and len(Definicion)):

            if(VerificarPalabra(AgregarPalabra)):
                print("\nEsta palabra ya existe ¡por favor! agregue otra palabra")
            else:
                collection.insert_one({
                    "palabra": AgregarPalabra,
                    "definicion": Definicion
                })
        else:
            print("\n Por favor llenar ambos campos de informacion")

    elif(Opcion == 2):
        AgregarPalabra = input("\nIngrese la palabra que desea modificar: \n")

        NewWord = input("\nIngrese el nuevo valor de esta palabra: \n")

        NewDefinition = input("\nIngrese la nueva definicion de la palabra: \n")

        if(len(NewWord) and len(NewDefinition) and len(AgregarPalabra)):
            if(VerificarPalabra(AgregarPalabra)):
                Actualizar(AgregarPalabra, NewWord, NewDefinition)
            else:
                print("\n La palabra no existe!, vuelva a intentarlo")

        else:
            print("\n Por favor llenar los campos de informacion")

    elif(Opcion == 3):
        AgregarPalabra = input("\n Ingrese la palabra que desea eliminar \n")

        if(len(AgregarPalabra)):
            if(VerificarPalabra(AgregarPalabra)):
                Borrar(AgregarPalabra)

            else:
                print("\n La palabra no existe!")

        else:
            print("\n Por favor llenar los campos de informacion")

    elif(Opcion == 4):
        Mostrar()
    elif(Opcion == 5):
        AgregarPalabra = input("\n Ingrese la palabra que desea ver su significado \n")
        if(len(AgregarPalabra)):
            if(VerificarPalabra(AgregarPalabra)):
                getPalabra = collection.find_one({"palabra": AgregarPalabra})
                print(f'\nLa definicion es: {getPalabra["definicion"]}')
            else:
                print("\n La palabra no existe!")

        else:
            print("\n Por favor llenar los campos de informacion")

    elif(Opcion == 0):
        break

    else:
        print("\n Ingrese una opcion valida \n")  