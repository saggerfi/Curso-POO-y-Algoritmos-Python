
class Automovi:

    def __init__(self, modelo, marca, color):
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self._estado = 'en reposo'
        self._motor = Motor(cilindros = 4)
        self._frenos = Frenos(tipo = 5) 
    
    def acelerar(self, tipo = 'despacio'):
        if tipo == 'rapida':
            self._motor.inyecta_gasolina(10)
        else:
            self._motor.inyecta_gasolina(3)
        
        self._estado = 'en_movimiento'
    
    def frenar(self, tipo = 'ABS'):
        if tipo == 'otro':
            self._frenos.activar_frenos(10)
        else:
            self._frenos.activar_frenos(5)
        
        self._estado = 'frenando'

class Motor:

    def __init__(self, cilindros, tipo = 'gasolina'):
        self.cilindros = cilindros
        self.tipo = tipo
        self._temperatura = 0

    def inyecta_gasolina(self, cantidad):
        pass 

class Frenos:

    def __init__(self, tipo):
        self.tipo = tipo
    
    def activar_frenos(self, tiempo):
        pass