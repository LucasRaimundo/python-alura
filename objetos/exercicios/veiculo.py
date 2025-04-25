class Veiculo:
    def __init__(self, marca, modelo):
        self._marca = marca,
        self._modelo = modelo
        self._ligado = False

    def __str__(self):
        return self.modelo.ljust(25), self.marca.ljust(25), self._ligado