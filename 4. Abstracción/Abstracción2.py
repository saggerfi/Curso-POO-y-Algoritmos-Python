
class PS4:

    def __init__(self):
        pass

    def encender(self, usuario = 'Sagger', control = '75%', juego = 'The Last of Us part 2, Resident Evil 3 Remake, Uncharted A Legacy Collection'):
        self._cargar_pantalla_de_inicio()
        self._bienvenida(usuario)
        self._cargar_home()
        self._mostrar_bateria_del_control(control)
        self._desplegar_juegos(juego)
    
    def _cargar_pantalla_de_inicio(self):
        print('Cargando')
    
    def _bienvenida(self, usuario):
        print(f'Te damos la bienvenida de nuevo a Playstation, {usuario}')

    def _cargar_home(self):
        print('Cargando')

    def _mostrar_bateria_del_control(self, control):
        print(f'La bateria del contro es del {control}')
    
    def _desplegar_juegos(self, juegos):
        print(f'Tus juegos {juegos}')

if __name__ == '__main__':
    jugar = PS4()
    jugar.encender()


    