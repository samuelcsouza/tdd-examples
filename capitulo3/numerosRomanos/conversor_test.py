from capitulo3.numerosRomanos.conversor import ConversorNumeroRomano


class TestConversorNumerosRomanos():

    def test_entender_o_simbolo_I(self):
        conversor = ConversorNumeroRomano()

        numero = conversor.converte("I")

        assert 1 == numero
