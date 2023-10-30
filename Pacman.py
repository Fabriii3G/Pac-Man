#Modelo de objetos de la clase pacman
class Pacman:
    #Atributos de la clase pacman
    pacman = None
    def __init__(self, Estado, PosX, PosY, Velocidad):
        self.Estado = Estado
        self.PosX = PosX
        self.PosY = PosY
        self.Velocidad = Velocidad
    #Metodos de la clase pacman
    @staticmethod
    def get_instance(self):
        if self.pacman == None:
            self.pacman = Pacman("Vivo", 0, 0, 1)
        return self.pacman
    def mover_izquierda(self):
        None
    def mover_derecha(self):
        None
    def mover_arriba(self):
        None
    def mover_abajo(self):
        None
