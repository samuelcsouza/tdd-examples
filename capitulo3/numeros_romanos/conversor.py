class ConversorNumeroRomano():

    def converte(self, numero_romano: str) -> int:
        if numero_romano == "I":
            return 1
        elif numero_romano == "V":
            return 5

        return 0
