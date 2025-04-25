from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, ligado, portas):
        super().__init__(marca, modelo, ligado)
        self._portas = portas

    def __str__(self):
        super().__str__(self._portas)