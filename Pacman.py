#Modelo de objetos de la clase pacman
class Pacman:
    #Atributos de la clase pacman
    def __init__(self, Estado, PosX, PosY, Velocidad):
        self.Estado = Estado
        self.PosX = PosX
        self.PosY = PosY
        self.Velocidad = Velocidad
    #Metodos de la clase pacman

    def set_estado(self, estado):
        self.Estado=estado
    def mover_izquierda(self):
        self.PosX-=1
    def mover_derecha(self):
        self.PosX+=1
    def mover_arriba(self):
        self.PosY-=1
    def mover_abajo(self):
       self.PosY+=1