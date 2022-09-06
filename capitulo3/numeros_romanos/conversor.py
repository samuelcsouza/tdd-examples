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
        last_neighbor_right = 0

        for index in range(len(roman_number) - 1, -1, -1):
            number = roman_number[index]
            actual = self._table[number]
            multiplier = 1

            if actual < last_neighbor_right:
                multiplier = -1

            accumulator += actual * multiplier

            last_neighbor_right = actual

        return accumulator
