
class Gato:

    def __init__(self, **kwargs) -> None:
        self.nombre:str = kwargs.get("arma", None)
    
    def __str__(self) -> str:
        return f"Hola me llamo {self.nombre} y soy un gato normal"
    
class GatoGuerrero(Gato):

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.arma:str = kwargs.get("arma", None)

    def __str__(self) -> str:
        return f"Hola soy {self.nombre} y soy un gato guerrero que usa la arma {self.arma}"
    
class GatoMago(Gato):

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.hechizo:str = kwargs.get("arma", None)

    def __str__(self) -> str:
        return f"Hola soy {self.nombre} y soy un gato mago que el hechizo {self.hechizo}"
    
def evolucionar(Gato):

    print("Iniciando proceso de evolucion..." + "\n")
    evolucion:object = input("Elije el tipo de gato al que quieres que evolucione (Gerrero o Mago):")

    if evolucion == "Guerrero":
        Gato:object = GatoGuerrero(arma = "Lanza")
        print("Proceso de evolucion listo..." + "\n")
        return(Gato)

if __name__ == "__main__":

    Gato_Pixy = Gato(Nombre = "Pixy")
    Gato_Pixy = evolucionar(Gato_Pixy)
    print(Gato_Pixy)
