#Modelo de objetos de la clase pacman
class Pacman:
    #Atributos de la clase pacman
    def __init__(self, Estado, PosX, PosY, Velocidad):
        self.Estado = Estado
        self.PosX = PosX
        self.PosY = PosY
        self.Velocidad = Velocidad
    #Metodos de la clase pacman
    def set_estado(self, estado): # metodo de definir estado de pacman
        self.Estado=estado
    def mover_izquierda(self): # metodo mover izquierda
        self.PosX-=1
    def mover_derecha(self): # metodo mover derecha
        self.PosX+=1
    def mover_arriba(self): # metodo mover arriba
        self.PosY-=1
    def mover_abajo(self): # metodo mover abajo
       self.PosY+=1