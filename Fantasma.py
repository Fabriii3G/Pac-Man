import random
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
    def set_estado(self, estado):
        self.Estado=estado
    def mover_izquierda(self):
        self.PosY_Fantasma -= 1

    def mover_derecha(self):
        self.PosX_Fantasma += 1

    def mover_arriba(self):
        self.PosY_Fantasma -= 1

    def mover_abajo(self):
        self.PosY_Fantasma += 1

    def prueba(self):
        print("funciona")
