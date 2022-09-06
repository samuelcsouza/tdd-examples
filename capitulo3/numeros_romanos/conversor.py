class ConversorNumeroRomano():

    _tabela = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    def converte(self, numero_romano: str) -> int:
        return self._tabela[numero_romano]
