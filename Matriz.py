import random
import time
import threading
from Fantasma import Fantasma

class Matriz:
    def __init__(self, matriz, Pacman, Fantasmas):
        self.matriz = matriz
        self.pacman = Pacman
        self.fantasmas = Fantasmas
        self.puntos = 0
        self.posicionesPacman= [self.pacman.PosX, self.pacman.PosY]
        self.comerFantasmas = False
        self.finJuego = False
        self.pausa = False
        self.segundo_nivel = False
        self.nivel=1

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
        for fila in self.matriz:
            for elemento in fila:
                print(elemento, end="\t")
            print()
        print(f"PosicionX_Pacman:{self.pacman.PosX}, PosicionY_Pacman: {self.pacman.PosY}")
        print(f"Puntos: {self.puntos}")
        print("-------------------------------")

    # metodo de puntaje
    def puntaje(self):
        if self.matriz[self.pacman.PosY][self.pacman.PosX] == 1:
            self.puntos += 10
            self.matriz[self.pacman.PosY][self.pacman.PosX] = 4 # Elimina el punto de la celda
        elif self.matriz[self.pacman.PosY][self.pacman.PosX] == 3:
            self.puntos += 50

    def capsula(self):
        if self.matriz[self.pacman.PosY][self.pacman.PosX] == 2:
            self.comerFantasmas = True
            self.puntos +=100
            time.sleep(10)
            self.comerFantasmas = False
            print('si')


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
    def reiniciar(self):
        if not self.segundo_nivel:
            self.matriz= [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 4, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 0],
                          [0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0],
                          [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0],
                          [0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0],
                          [0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 3, 1, 0],
                          [0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0],
                          [0, 1, 0, 1, 0, 0, 2, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0],
                          [0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0],
                          [0, 1, 1, 1, 1, 1, 1, 0, 2, 0, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0],
                          [0, 0, 1, 0, 0, 0, 1, 0, 2, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0],
                          [0, 0, 3, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 4, 4, 4, 4, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0],
                          [0, 0, 0, 0, 1, 0, 1, 0, 2, 0, 1, 0, 0, 4, 4, 4, 4, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0],
                          [0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0],
                          [0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 3, 0],
                          [0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0],
                          [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                          [0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                          [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                          [0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0],
                          [0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0],
                          [0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0],
                          [0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0],
                          [0, 2, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 2, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
            fantasma1 = Fantasma("Vivo", 13, 11, "R", 1)  # 13, 12 posicion
            fantasma2 = Fantasma("Vivo", 13, 12, "C", 1)  # 13, 12 posicion
            fantasma3 = Fantasma("Vivo", 15, 11, "N", 1)  # 13, 12 posicion
            fantasma4 = Fantasma("Vivo", 15, 12, "r", 1)  # 13, 12 posicion
            fantasma5 = Fantasma("Vivo", 15, 11, "N", 1)  # 13, 12 posicion
            fantasma6 = Fantasma("Vivo", 13, 11, "R", 1)  # 13, 12 posicion
            self.pacman.PosY=1
            self.pacman.PosX=1
            self.fantasmas = [fantasma1, fantasma2, fantasma3, fantasma4, fantasma5, fantasma6]
            self.finJuego = False
            self.hilo()
            self.nivel = 2
            self.segundo_nivel = True