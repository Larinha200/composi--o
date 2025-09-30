class Processador:
    def __init__(self, modelo, velocidade_ghz):
        self.__modelo = modelo
        self.__velocidade_ghz = velocidade_ghz
    
    def getModelo(self):
        return self.__modelo 
    
    def getVelocidade_ghz(self):
        return self.__velocidade_ghz 
    
    def __str__(self):
        return f'Modelo:{self.__modelo} \nVelocidade ghz:{self.__velocidade_ghz }'


class Memoria_RAM:
    def __init__(self,capacidade_gb, tipo):
        self.__capacidade_gb = capacidade_gb
        self.__tipo = tipo

    def getCapacidade_gb(self):
        return self.__capacidade_gb
    
    def getTipo(self):
        return self.__tipo
    
    def __str__(self):
        return f'Capacidade gb: {self.__capacidade_gb} \nTipo: {self.__tipo}'
    
class Armazenamento:
    def __init__(self, tipo, capacidade_gb):
        self.__tipo = tipo
        self.__capacidade_gb = capacidade_gb

    def getTipo(self):
        return self.__tipo
    
    def getCapacidade_gb(self):
        return self.__capacidade_gb
    
    def __str__(self):
        return f'Tipo: {self.__tipo} \nCapacidade gb: {self.__capacidade_gb}'
    
class Computador:
    def __init__(self, marca, modelo):
        self.__marca = marca
        self.__modelo = modelo
        self.__processador = Processador()
        self.__memoria_RAM = Memoria_RAM()
        self.__armazenamento = Armazenamento()

    def getMarca(self):
        return self.__marca
    
    def getModelo(self):
        return self.__modelo
    
    def __str__(self):
        return f'Marca: {self.__marca} \nModelo: {self.__modelo} \nProcessador: \nModelo: {self.__processador.getModelo} \nVelocidade ghz: {self.__processador.getVelocidade_ghz} \nMemoria RAM: \nCpacidade gb:{self.__memoria_RAM.getCapacidade_gb} \ntipo: {self.__memoria_RAM.getTipo} \nArmezenamento: \nCapacidade gb: {self.__armazenamento.getCapacidade_gb} \nTipo: {self.__armazenamento.getTipo}'
    
    
    def ligar (self):
        self.getMarca 
        self.getModelo
        self.__processador.getModelo
        self.__processador.getVelocidade_ghz
        self.__memoria_RAM.getCapacidade_gb
        self.__memoria_RAM.getTipo
        self.__armazenamento.getCapacidade_gb
        self.__armazenamento.getTipo
        return self.getMarca ,self.getModelo,self.__processador.getModelo,self.__processador.getVelocidade_ghz,self.__memoria_RAM.getCapacidade_gb,self.__memoria_RAM.getTipo,self.__armazenamento.getCapacidade_gb,self.__armazenamento.getTipo
    