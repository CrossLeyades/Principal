
class RUT:

    id = 1

    def __init__(self, **kwargs) -> None:
        
        self.nombre = kwargs.get("nombre", None)
        self.edad = kwargs.get("edad", None)
        self.sexo = kwargs.get("sexo", None)
        self.__id = RUT.id

        RUT.id += 1

    def __str__(self) -> str:
        return f"Hola mi nombre es {self.nombre} y mi id es {self.__id}"

if __name__ == "__main__":

    Jose = RUT(nombre = "Jose", edad = 32, sexo = "Masculino")

    print(Jose._RUT__id)