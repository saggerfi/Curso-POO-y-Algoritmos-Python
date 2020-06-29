class Hotel:
    def añadir_huespedes(self, cantidad_de_huespedes):
        self.huespedes += cantidad_de_huespedes
    
    def checkout(self, cantidad_de_huespedes):
        self.huespedes -= cantidad_de_huespedes

    def ocupación_total(self):
        return self.huespedes

hotel = Hotel(50, 20)
hotel.añadir_huespedes(3)
hotel.checkout(1)
hotel.ocupación_total() #2