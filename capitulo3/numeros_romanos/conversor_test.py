from capitulo3.numeros_romanos.conversor import ConversorNumeroRomano


class TestConversorNumerosRomanos():

    def test_entender_o_simbolo_I(self):
        conversor = ConversorNumeroRomano()

        numero = conversor.converte("I")

        assert 1 == numero

    def test_entender_o_simbolo_V(self):
        conversor = ConversorNumeroRomano()
        numero = conversor.converte("V")

        assert 5 == numero
