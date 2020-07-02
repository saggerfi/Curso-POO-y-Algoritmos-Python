
class Lavadora:
    
    def __init__(self):
        pass

    def lavar(self, temperatura = 'caliente'):
        self._llenar_tanque_de_agua(temperatura)
        self._añadir_jabon()
        self._lavar()
        self._centrifugar()

    def _llenar_tanque_de_agua(self, temperatura):
        print(f'Llenando tanque con agua {temperatura}')

    def _añadir_jabon(self):
        print('Añadiendo jabón')

    def _lavar(self):
        print('Lavando ropa')
    
    def _centrifugar(self):
        print('Centrifugando')

if __name__ == '__main__' :
    lavadora = Lavadora()
    lavadora.lavar()
