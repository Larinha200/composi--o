class Processador:
    def __init__(self, modelo_pro, velocidade_ghz_pro):
        self.__modelo_pro = modelo_pro
        self.__velocidade_ghz_pro = velocidade_ghz_pro
    
    def getModelo_pro(self):
        return self.__modelo_pro
    
    def getVelocidade_ghz_pro(self):
        return self.__velocidade_ghz_pro 
    
    def __str__(self):
        return f'Modelo:{self.__modelo_pro} \nVelocidade ghz:{self.__velocidade_ghz_pro }'


class Memoria_RAM:
    def __init__(self,capacidade_gb_RAM, tipo_RAM):
        self.__capacidade_gb_RAM = capacidade_gb_RAM
        self.__tipo_RAM = tipo_RAM

    def getCapacidade_gb(self):
        return self.__capacidade_gb_RAM
    
    def getTipo(self):
        return self.__tipo_RAM
    
    def __str__(self):
        return f'Capacidade gb: {self.__capacidade_gb_RAM} \nTipo: {self.__tipo_RAM}'
    
class Armazenamento:
    def __init__(self, tipo_ar, capacidade_gb_ar):
        self.__tipo_ar = tipo_ar
        self.__capacidade_gb_ar = capacidade_gb_ar

    def getTipo_ar(self):
        return self.__tipo_ar
    
    def getCapacidade_gb_ar(self):
        return self.__capacidade_gb_ar
    
    def __str__(self):
        return f'Tipo: {self.__tipo_ar} \nCapacidade gb: {self.__capacidade_gb_ar}'
    
class Computador:
    def __init__(self, marca, modelo,modelo_pro,velocidade_ghz_pro,capacidade_gb_RAM,tipo_RAM,tipo_ar, capacidade_gb_ar):
        self.__marca = marca
        self.__modelo = modelo
        self.__processador = Processador(modelo_pro, velocidade_ghz_pro)
        self.__memoria_RAM = Memoria_RAM(capacidade_gb_RAM , tipo_RAM)
        self.__armazenamento = Armazenamento(tipo_ar, capacidade_gb_ar)

    def getMarca(self):
        return self.__marca
    
    def getModelo(self):
        return self.__modelo
    
    def __str__(self):
        return f'Marca: {self.__marca} \nModelo: {self.__modelo} \nProcessador: \nModelo: {self.__processador.getModelo_pro()} \nVelocidade ghz: {self.__processador.getVelocidade_ghz_pro()} \nMemoria RAM: \nCpacidade gb:{self.__memoria_RAM.getCapacidade_gb()} \ntipo: {self.__memoria_RAM.getTipo()} \nArmezenamento: \nCapacidade gb: {self.__armazenamento.getCapacidade_gb()} \nTipo:{self.__armazenamento.getTipo()}'
    
    
    def ligar (self):
        self.getMarca 
        self.getModelo
        self.__processador.getModelo_pro
        self.__processador.getVelocidade_ghz_pro
        self.__memoria_RAM.getCapacidade_gb_RAM
        self.__memoria_RAM.getTipo_RAM
        self.__armazenamento.getCapacidade_gb_ar
        self.__armazenamento.getTipo_ar
        return self.getMarca ,self.getModelo,self.__processador.getModelo_pro,self.__processador.getVelocidade_ghz_pro,self.__memoria_RAM.getCapacidade_gb_RAM,self.__memoria_RAM.getTipo_RAM,self.__armazenamento.getCapacidade_gb_ar,self.__armazenamento.getTipo_ar
    