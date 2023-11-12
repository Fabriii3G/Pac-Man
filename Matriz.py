import random
import time
import threading
from Fantasma import Fantasma

#Modelo de objetos de la clase Matriz
class Matriz:
    #Atributos de la clase matriz
    def __init__(self, matriz, Pacman, Fantasmas):
        self.matriz = matriz
        self.pacman = Pacman
        self.fantasmas = Fantasmas
        self.puntos = 0
        self.posicionesPacman= [self.pacman.PosX, self.pacman.PosY]
        self.comerFantasmas = False #Atributo booleano que indica si el pacman puede comer fantasmas
        self.finJuego = False #Atributo booleano que indica el final de juego
        self.pausa = False #Atributo booleano que indica la pausa
        self.segundo_nivel = False #Atributo booleano que indica el segundo nivel
        self.nivel = 1 #Atributo para indicar en que nivel se esta
        self.comer = "No" #Atributo para indicar en pantalla si se puede comer fantasmas

    # metodo que actualiza la matriz
    def actualizar_matriz(self):
        # Buscar y eliminar el emoji anterior de Pac-Man en la matriz
        for n in range(len(self.matriz)):
            for j in range(len(self.matriz[0])):
                if self.matriz[n][j] == "🟡":
                    self.matriz[n][j] = 4  # Reemplazar "🟡" por 4
                elif self.matriz[n][j] == "R" or self.matriz[n][j] == "C" or self.matriz[n][j] == "N" or self.matriz[n][j] == "r":
                    self.matriz[n][j] = 1 # Reemplazar fantasmas por 1
        # Colocar el emoji de Pac-Man en su nueva posición
        self.matriz[self.pacman.PosY][self.pacman.PosX] = "🟡"
        for fantasma in self.fantasmas:
            self.matriz[fantasma.PosY_Fantasma][fantasma.PosX_Fantasma] = fantasma.Color


    # metodo que imprime la matriz
    def imprimir_matriz(self):
        self.actualizar_matriz()
        for n in self.matriz:
            for j in n:
                print(j, end="\t")
            print()
        print(f"PosicionX_Pacman:{self.pacman.PosX}, PosicionY_Pacman: {self.pacman.PosY}")
        print(f"Puntos: {self.puntos}")
        for fantasma in self.fantasmas:
            print(f"Color: {fantasma.Color}, PosicionX_Fantasma:{fantasma.PosX_Fantasma}, PosicionY_Fantasma: {fantasma.PosY_Fantasma}")
        print("------------------------------------------------------------------------------------------------------------------------")

    # metodo de puntaje
    def puntaje(self):
        if self.matriz[self.pacman.PosY][self.pacman.PosX] == 1:
            self.puntos += 10 # Anade 10 puntos
            self.matriz[self.pacman.PosY][self.pacman.PosX] = 4 # Elimina el punto de la celda
        elif self.matriz[self.pacman.PosY][self.pacman.PosX] == 3:
            self.puntos += 50 # Anade 50 puntos

    # metodo de comer capsula
    def capsula(self):
        if self.matriz[self.pacman.PosY][self.pacman.PosX] == 2:
            self.comerFantasmas = True
            self.comer = "Si"
            self.puntos +=100
            time.sleep(10)
            self.comerFantasmas = False
            self.comer = "No"

    # metodo que detecta si hay pared antes de hacer el movimiento
    def detectar_colision_pared(self, x, y):
        return self.matriz[y][x] == 0 #Retorna el valor booleano si la posicion ingresada es una pared

    # metodo que detecta la colision entre pacman y los fantasmas
    def colision_pacman_y_fantasmas(self):
        i = 0
        if self.comerFantasmas==False:
            while i<len(self.fantasmas):
                if self.pacman.PosX == self.fantasmas[i].PosX_Fantasma and self.pacman.PosY == self.fantasmas[i].PosY_Fantasma:
                    self.matriz[self.posicionesPacman[1]][self.posicionesPacman[0]] = 1
                    self.pacman.set_estado("Muerto")
                    print("Pacman ha muerto")
                    return True
                i +=1
        elif self.comerFantasmas==True:
            while i < len(self.fantasmas):
                if self.pacman.PosX == self.fantasmas[i].PosX_Fantasma and self.pacman.PosY == self.fantasmas[i].PosY_Fantasma:
                    self.matriz[self.fantasmas[i].PosY_Fantasma][self.fantasmas[i].PosX_Fantasma] = 4
                    self.fantasmas.remove(self.fantasmas[i])
                    print("Fantasma muerto")
                    self.puntos += 200
                    return True
                i += 1


    # metodo para hilo que se encarga del movimiento de los fantasmas
    def hilo(self):
        hilo = threading.Thread(target=self.mover_fantasma)
        hilo.daemon = True
        hilo.start()

    # metodo para elegir la direccion en la que se mueve el fantasma
    def mover_fantasma(self):
        while not self.finJuego:
            i=0
            if not self.pausa:
                while i<len(self.fantasmas):
                    try:
                        columnas = 29
                        filas = 25
                        direccion = random.choice(['Derecha', 'Izquierda', 'Abajo', 'Arriba'])
                        if direccion == 'Derecha' and self.fantasmas[i].PosX_Fantasma + 1 < columnas:
                            if not self.detectar_colision_pared(self.fantasmas[i].PosX_Fantasma + 1, self.fantasmas[i].PosY_Fantasma):
                                self.colision_pacman_y_fantasmas()
                                self.fantasmas[i].PosX_Fantasma += 1
                        elif direccion == 'Izquierda' and self.fantasmas[i].PosX_Fantasma - 1 >= 0:
                            if not self.detectar_colision_pared(self.fantasmas[i].PosX_Fantasma - 1, self.fantasmas[i].PosY_Fantasma):
                                self.colision_pacman_y_fantasmas()
                                self.fantasmas[i].PosX_Fantasma -= 1
                        elif direccion == 'Abajo' and self.fantasmas[i].PosY_Fantasma + 1 < filas:
                            if not self.detectar_colision_pared(self.fantasmas[i].PosX_Fantasma, self.fantasmas[i].PosY_Fantasma + 1):
                                self.colision_pacman_y_fantasmas()
                                self.fantasmas[i].PosY_Fantasma += 1
                        elif direccion == 'Arriba' and self.fantasmas[i].PosY_Fantasma - 1 >= 0:
                            if not self.detectar_colision_pared(self.fantasmas[i].PosX_Fantasma, self.fantasmas[i].PosY_Fantasma - 1):
                                self.colision_pacman_y_fantasmas()
                                self.fantasmas[i].PosY_Fantasma -= 1
                        i+=1
                        time.sleep(0.05)
                    except:
                        pass


    # metodo reiniciar cuando se pasa el primer nivel
    def reiniciar(self):
        if not self.segundo_nivel:
            self.matriz= [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 4, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 2, 0, 0, 2, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 2, 0],
                          [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
                          [0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0],
                          [0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
                          [0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0],
                          [0, 1, 0, 1, 1, 1, 1, 0, 1, 2, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 2, 1, 0, 3, 1, 1, 1, 0, 1, 0],
                          [0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0],
                          [0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0],
                          [0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0],
                          [0, 0, 1, 0, 0, 0, 2, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 2, 0, 0, 0, 1, 0, 0],
                          [0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0],
                          [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0],
                          [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0],
                          [0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0],
                          [0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0],
                          [0, 3, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 3, 1, 1, 3, 0],
                          [0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0],
                          [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                          [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 0],
                          [0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
                          [0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0],
                          [0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
                          [0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0],
                          [0, 2, 1, 1, 1, 1, 2, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 2, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
            fantasma1 = Fantasma("Vivo", 15, 13, "R", 1)
            fantasma2 = Fantasma("Vivo", 15, 12, "C", 1)
            fantasma3 = Fantasma("Vivo", 15, 12, "N", 1)
            fantasma4 = Fantasma("Vivo", 15, 13, "r", 1)
            fantasma5 = Fantasma("Vivo", 13, 17, "N", 1)
            fantasma6 = Fantasma("Vivo", 13, 17, "R", 1)
            self.pacman.PosY=1
            self.pacman.PosX=1
            self.fantasmas = [fantasma1, fantasma2, fantasma3, fantasma4, fantasma5, fantasma6]
            self.finJuego = False
            self.hilo()
            self.nivel = 2
            self.segundo_nivel = True