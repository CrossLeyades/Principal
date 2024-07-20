
from collections import namedtuple
from random import shuffle, choice, randint  # Puedes utilizar estas funciones si lo deseas

# Definimos la clase juego
class Juego:

    # Definimos el constructor
    def __init__(self, turnos):

        # Definimos parametros
        self.mazo: list = []
        self.cartas_j1: list = []
        self.cartas_j2: list = []

        self.read_file() # Leemos archivo
        self.repartir_cartas() # Repartimos cinco cartas
        self.comenzar_juego(turnos) # Iniciamos el bucle de  juego

    def read_file(self):
        # Leer las cartas y guardarlas en una estructura de datos adecuada
         with open('cards.csv', 'r', encoding="utf-8", errors='replace') as archivo:
             
             Carta: namedtuple = namedtuple("Carta", ["nombre", "ataque", "defensa"])
             linea: str = archivo.readline()

             while linea:
                 linea: str = archivo.readline()
                 lista: list = linea.split(",")
                 if len(lista) == 3:
                    carta: namedtuple = Carta(lista[0], int(lista[1]), int(lista[2]))
                    self.mazo.append(carta)

    def repartir_cartas(self):
        # Barajar las cartas y repartirlas de a 1
        for _ in range(5):
            carta = self.mazo.pop(randint(0, len(self.mazo) - 1))
            self.cartas_j1.append(carta)
            carta = self.mazo.pop(randint(0, len(self.mazo) - 1))
            self.cartas_j2.append(carta)

    def atacar(self, atacante, defensa):
        
        ptos_ataque = atacante.ataque
        ptos_defensa = defensa.defensa
        return (ptos_defensa - ptos_ataque)

    def comenzar_juego(self, turnos):
        
        for i in range(1, turnos + 1):
            
            print(f"Turno número {i}")

            print(f"Mano jugador 1: {[carta.nombre for carta in self.cartas_j1]}")
            print(f"Mano jugador 2: {[carta.nombre for carta in self.cartas_j2]}" + "\n")

            carta_1 = self.cartas_j1.pop(randint(0, len(self.cartas_j1) - 1))
            carta_2 = self.cartas_j2.pop(randint(0, len(self.cartas_j2) - 1))
            
            if i % 2:
                # Ataca el jugador 1
                print(f"El jugador 1 ataca con {carta_1.nombre} con {carta_1.ataque}")
                print(f"El jugador 2 defiende con {carta_2.nombre} con {carta_2.defensa}" + "\n")

                resultado = self.atacar(carta_1, carta_2)

                if resultado < 0: 
                    print("Jugador 1 gana la ronda" + "\n")
                    self.cartas_j1.append(carta_1)
                else:
                    print("Jugador 2 gana la ronda" + "\n")
                    self.cartas_j2.append(carta_2)
            else:
                # Ataca el jugador 2
                print(f"El jugador 2 ataca con {carta_2.nombre} con {carta_2.ataque}")
                print(f"El jugador 1 defiende con {carta_1.nombre} con {carta_1.defensa}" + "\n")

                resultado = self.atacar(carta_2, carta_1)

                if resultado < 0: 
                    print("Jugador 2 gana la ronda" + "\n")
                    self.cartas_j2.append(carta_2)
                else:
                    print("Jugador 1 gana la ronda" + "\n")
                    self.cartas_j1.append(carta_1)
            
            # Si alguno de los jugadores se queda sin cartas, termina la partida
            if not (len(self.cartas_j1) and len(self.cartas_j2)):
                
                print('Ha terminado la partida')
                
                if len(self.cartas_j1) == 0:
                    print("El ganador es el jugador 2")
                else:
                    print("El ganador es el jugador 1")
                break

if __name__ == "__main__":
    juego = Juego(10)