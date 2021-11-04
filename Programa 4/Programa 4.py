import redis
PalabraClave = "Palabra"
DefinicionClave = "Defincion"
#Michael Castillo 8-963-1499
#Programacion 4
r = redis.Redis(host='127.0.0.1', port=6379)
r.set("id", -1)
print(r.keys())


def Verificar(Palabra):
    CantPalabras = r.llen(PalabraClave)
    PalabraExistente = False
    for i in range(CantPalabras):
        PalabraActual = r.lindex(PalabraClave, i).decode('utf-8')
        if(PalabraActual == Palabra):
            PalabraExistente = True
            break
    return PalabraExistente


def Agregar(Palabra,Definicion):
    r.incr("id")
    r.rpush(PalabraClave, Palabra)
    r.rpush(DefinicionClave, Definicion)
    print("\n ¡Palabra agregada correctamente!")


def Actualizar(AntiguaPalabra, NuevaPalabra, NuevaDefinicion):
    CantPalabras = r.llen(PalabraClave)
    for i in range(CantPalabras):
        PalabraActual = r.lindex(PalabraClave, i).decode('utf-8')
        if(PalabraActual == AntiguaPalabra):
            r.lset(PalabraClave, i, NuevaPalabra)
            r.lset(DefinicionClave, i, NuevaDefinicion)
            break

    print("\n¡Palabra" + AntiguaPalabra+ "actualizada!")


def Borrar(Palabra):
    CantPalabras = r.llen(PalabraClave)
    for i in range(CantPalabras):
        PalabraActual = r.lindex(PalabraClave, i).decode('utf-8')
        DefinicionActual = r.lindex(DefinicionClave, i).decode('utf-8')
        if(PalabraClave == Palabra):
            r.lrem(PalabraClave, i, PalabraActual)
            r.lrem(DefinicionClave, i, DefinicionActual)
            break
    print("\n ¡Palabra eliminada!")


def MostrarPalabras():
    CantPalabras = r.llen(PalabraClave)
    for i in range(CantPalabras):
        print(f'{i + 1}. Palabra: {r.lindex(PalabraClave, i).decode("utf-8")} \n Definicion: {r.lindex(DefinicionClave, i).decode("utf-8")}')


while True:

   
    print("\n****Diccionario Slang****")
    print("\nIngrese opción: \n")

    Opcion = int(input(" 1). Agregar nueva palabra \n 2). Editar palabra \n 3). Eliminar palabra \n 4). Ver listado de palabras \n 5). Saber significado de la palabra \n 6). Salir \n"))

    if(Opcion == 1):

        EntradaPalabra = input("\nIngrese la palabra:\n")
        EntradaDefinicion = input(
            "\nIngrese definición: \n")
        if(len(EntradaPalabra) and len(EntradaDefinicion)):
            if(Verificar(EntradaPalabra)):
                print("\nPalabra existente, ¡Por favor! ingrese otra palabra:")
            else:
                Agregar(EntradaPalabra, EntradaDefinicion)
        else:
            print("\n¡Por favor! llene los campos de información:")

    elif(Opcion == 2):
        EntradaPalabra = input("\nIngrese palabra a modificar: \n")

        NewWord = input("\nIngrese el nuevo valor de esta palabra:\n")

        NewDefinition  = input(
            "\nIngrese nueva definición de la palabra:\n")

        if(len(NewWord) and len(NewDefinition) and len(EntradaPalabra)):
            if(Verificar(EntradaPalabra)):
                Actualizar(EntradaPalabra, NewWord, NewDefinition)
            else:
                print("\n¡Esta palabra no existe!, vuelva a intentarlo")

        else:
            print("\n¡Por favor! llene los campos de información:")

    elif(Opcion == 3):
        EntradaPalabra = input("\nIngrese palabra a eliminar:")

        if(len(EntradaPalabra)):
            if(Verificar(EntradaPalabra)):
                Borrar(EntradaPalabra)

            else:
                print("\n¡Esta palabra no existe!")

        else:
            print("\n¡Por favor! llene los campos de información:")

    elif(Opcion == 4):
        MostrarPalabras()
    elif(Opcion == 5):
        EntradaPalabra = input("\nIngrese palabra que desea ver su significado:\n")
        if(len(EntradaPalabra)):
            if(Verificar(EntradaPalabra)):
                cantPalabras = r.llen(PalabraClave)
                for i in range(cantPalabras):
                    PalabraActual = r.lindex(PalabraClave, i).decode('utf-8')
                    if(PalabraActual == EntradaPalabra):
                        print(
                            f'La definicion es: {r.lindex(DefinicionClave, i).decode("utf-8")}')
                        break

            else:
                print("\n¡Esta palabra no existe!")

        else:
            print("\n¡Por favor! llene los campos de información:")

    elif(Opcion == 6):
        break

    else:
        print("\nIngrese una opcion valida:\n")