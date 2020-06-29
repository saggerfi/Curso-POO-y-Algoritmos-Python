class Hotel:
    def __init__(self, numero_max_huespedes, lugares_estacionamiento):
        self.numero_max_huespedes = numero_max_huespedes
        self.lugares_estacionamiento = lugares_estacionamiento
        self.huespedes = 0

hotel = Hotel(numero_max_huespedes = 50, lugares_estacionamiento = 20)
print(hotel.lugares_estacionamiento) #20