class Carro(object):

    def __init__(self, portas, cor, marca, modelo, ano, kml):
        self.portas = portas
        self.cor = cor
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.rodas = 4
        self.kml = kml

    def anda(self, kilometros):
        return 'Meu ' + self.marca + ' ' + self.modelo + ' ' + self.cor + ' andou ' + str(kilometros) + 'km'

    def consumo(self, kilometros):
        return 'Minha ' + self.modelo + ' faz na cidade ' + str(kilometros / self.kml)