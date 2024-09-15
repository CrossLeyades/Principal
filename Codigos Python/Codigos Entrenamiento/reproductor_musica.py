
def crear_listas(ruta_cantantes = "doc\cantantes.txt", ruta_canciones = "doc\canciones.txt")->list:
    
    print(f"cargando datos de la ruta {ruta_cantantes}..." + "\n")
    lista_cantantes:list = []
    with open(ruta_cantantes, 'r', encoding='utf-8') as archvio:
        datos = archvio.readlines()
        for dato in datos:
            lista_cantantes.append(dato.strip("\n"))
    
    print(f"cargando datos de la ruta {ruta_canciones}..." + "\n")
    lista_canciones:list = []
    with open(ruta_canciones, 'r', encoding='utf-8') as archivo:
        datos = archivo.readlines()
        for dato in datos:
            lista_canciones.append(dato.strip("\n"))

    return( lista_cantantes, lista_canciones)

def crear_diccionario(lista_cantantes, lista_canciones) -> dict:
    
    print("Creando reproductor..." + "\n")
    diccionario:dict = {}
    for posicion in range(0, len(lista_canciones) - 1):
        diccionario[lista_cantantes[posicion]] = lista_canciones[posicion] 

    return(diccionario)

def usar_reproductor(reproductor):

    print("Cargarndo reproducor" + "\n")

    texto = f"""{reproductor.keys()}

            Indique el nombre del cantante que quiere reproducir:"""

    valor = input(texto)
    print(f"Cargando la cancion {reproductor[valor]} del cantante {valor}")

if __name__ == "__main__":
    
    print("\n" + "Iniciando programa..." + "\n")
    listas = crear_listas()
    reproductor = crear_diccionario(listas[0], listas[1])
    usar_reproductor(reproductor)
