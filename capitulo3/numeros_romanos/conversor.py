class ConversorNumeroRomano():

    _table = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    def converte(self, roman_number: str) -> int:
        accumulator = 0

        for number in roman_number:
            accumulator = accumulator + self._table[number]

        return accumulator
