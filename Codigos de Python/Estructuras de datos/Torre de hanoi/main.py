class TorreDeHanoi:

    def __init__(self):
        self.pilar_1 = [6, 5, 4, 3, 2, 1]
        self.pilar_2 = []
        self.pilar_3 = []

    def mover_disco(self, pilar_origen, pilar_destino):
    
        pieza = pilar_origen.pop()

        if pilar_destino == []:
            pilar_destino.append(pieza)
        elif pieza < pilar_destino[-1]:
            pilar_destino.append(pieza)
        else:
            print("La accion que tratas de hacer no cumple con las reglas" + "\n")
            pilar_origen.append(pieza)

    def __str__(self):
        output = ""
        # Range termina con -1 para recorrer al revés
        for i in range(5, -1, -1):
            fila = " "  # Armamos una fila a la vez, desde arriba
            # Pilar 1
            if len(self.pilar_1) > i:
                fila += str(self.pilar_1[i]) + " "
            else:
                fila += "x "
            # Pilar 2
            if len(self.pilar_2) > i:
                fila += str(self.pilar_2[i]) + " "
            else:
                fila += "x "
            # Pilar 3
            if len(self.pilar_3) > i:
                fila += str(self.pilar_3[i]) + " "
            else:
                fila += "x "
            output += fila + "\n"
        output += "=" * 7 + "\n"
        return output
    
if __name__ == "__main__":

    torres = TorreDeHanoi()

    torres.mover_disco(torres.pilar_1, torres.pilar_2)
    print(torres)
    torres.mover_disco(torres.pilar_1, torres.pilar_2)
    print(torres)