class Processador:
    def __init__(self, modelo, velocidade_ghz):
        self.__modelo = modelo
        self.__velocidade_ghz = velocidade_ghz

class Memoria_RAM:
    def __init__(self,capacidade_gb, tipo):
        self.__capacidade_gb = capacidade_gb
        self.__tipo = tipo

class Armazenamento:
    def __init__(self, tipo, capacidade_gb):
        self.__tipo = tipo
        self.__capacidade_gb = capacidade_gb

class Computador:
    def __init__(self, marca, modelo):
        self.__marca = marca
        self.__modelo = modelo
        self.__processador = Processador()
        self.__memoria_RAM = Memoria_RAM()
        self.__armazenamento = Armazenamento()
        