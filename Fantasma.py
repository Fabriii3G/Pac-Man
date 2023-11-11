#Modelo de objetos de la clase Fantasma
class Fantasma:
    #Atributos de la clase fantasma
    def __init__(self,Estado_Fantasma, PosX_Fantasma, PosY_Fantasma, Color, Velocidad_Fantasma):
        self.Estado_Fantasma = Estado_Fantasma
        self.PosX_Fantasma = PosX_Fantasma
        self.PosY_Fantasma = PosY_Fantasma
        self.Color = Color
        self.Velocidad_Fantasma = Velocidad_Fantasma

    #Metodos de la clase fantasma
    def mover_izquierda(self): # metodo mover izquierda
        self.PosY_Fantasma -= 1

    def mover_derecha(self): # metodo mover derecha
        self.PosX_Fantasma += 1

    def mover_arriba(self): # metodo mover arriba
        self.PosY_Fantasma -= 1

    def mover_abajo(self): # metodo mover abajo
        self.PosY_Fantasma += 1