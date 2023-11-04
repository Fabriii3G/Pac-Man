import random
import time
import threading

matrizJuego= [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
              [0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0],
              [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0],
              [0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0],
              [0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0],
              [0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0],
              [0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0],
              [0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0],
              [0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0],
              [0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0],
              [0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0],
              [0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0],
              [0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0],
              [0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0],
              [0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0],
              [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
              [0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
              [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
              [0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0],
              [0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0],
              [0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0],
              [0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0],
              [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
class Matriz:
    def __init__(self, matriz, Pacman, Fantasmas):
        self.matriz = matriz
        self.pacman = Pacman
        self.fantasmas = Fantasmas
        self.puntos = 0
        self.posicionesPacman= [self.pacman.PosX, self.pacman.PosY]
        #self.posicionesFantama = [self.fantasma.PosX_Fantasma, self.fantasma.PosY_Fantasma]

    def puntos(self):
        if self.posicionesPacman == 1:
            self.puntos+=1

    # metodo que actualiza la matriz
    def actualizar_matriz(self):
        # Buscar y eliminar el emoji anterior de Pac-Man en la matriz
        for n in range(len(self.matriz)):
            for j in range(len(self.matriz[0])):
                if self.matriz[n][j] == "🟡" or self.matriz[n][j] == "🔴":
                    self.matriz[n][j] = 1  # Reemplazar "🟡" por 1

        # Colocar el emoji de Pac-Man en su nueva posición
        self.matriz[self.pacman.PosY][self.pacman.PosX] = "🟡"
        i=0
        while i < len(self.fantasmas):
            self.matriz[self.fantasmas[i].PosY_Fantasma][self.fantasmas[i].PosX_Fantasma] = "🔴"
            i+=1

    # metodo que imprime la matriz
    def imprimir_matriz(self):
        print()
        self.actualizar_matriz()
        for fila in self.matriz:
            for elemento in fila:
                print(elemento, end="\t")
            print()
        print(f"PosicionX_Pacman:{self.pacman.PosX}, PosicionY_Pacman: {self.pacman.PosY}")
        #print(f"PosicionX_fantasma:{self.fantasma.PosX_Fantasma}, PosicionY_fantasma: {self.fantasma.PosY_Fantasma}")

        print("-------------------------------")

    # metodo para hilo que se encarga del movimiento de los fantasmas
    def hilo(self):
        hilo = threading.Thread(target=self.mover_fantasma())
        hilo.daemon = True
        hilo.start()

    # metodo que detecta si hay pared antes de hacer el movimiento
    def detectar_colision_pared(self, x, y):
        return self.matriz[y][x] == 0 #Retorna el valor booleano si la posicion ingresada es una pared

    # metodo que detecta la colision entre pacman y los fantasmas
    def colision_pacman_y_fantasmas(self):
        if self.pacman.PosY == self.fantasma.PosY_Fantasma and self.pacman.PosX == self.fantasma.PosX_Fantasma:
            self.matriz[self.posicionesPacman[1]][self.posicionesPacman[0]] = 1
            self.pacman.set_estado("Muerto")
            print("Pacman ha muerto")
            return True

    # metodo para elegir la direccion en la que se mueve el fantasma
    def mover_fantasma(self):
        while True:
            i=0
            while i<len(self.fantasmas):
                columnas = 29
                filas = 25
                direccion = random.choice(['Derecha', 'Izquierda', 'Abajo', 'Arriba'])
                if direccion == 'Derecha' and self.fantasmas[i].PosX_Fantasma + 1 < columnas:
                    if not self.detectar_colision_pared(self.fantasmas[i].PosX_Fantasma + 1, self.fantasmas[i].PosY_Fantasma):
                        self.fantasmas[i].PosX_Fantasma += 1
                elif direccion == 'Izquierda' and self.fantasmas[i].PosX_Fantasma - 1 >= 0:
                    if not self.detectar_colision_pared(self.fantasmas[i].PosX_Fantasma - 1, self.fantasmas[i].PosY_Fantasma):
                        self.fantasmas[i].PosX_Fantasma -= 1
                elif direccion == 'Abajo' and self.fantasmas[i].PosY_Fantasma + 1 < filas:
                    if not self.detectar_colision_pared(self.fantasmas[i].PosX_Fantasma, self.fantasmas[i].PosY_Fantasma + 1):
                        self.fantasmas[i].PosY_Fantasma += 1
                elif direccion == 'Arriba' and self.fantasmas[i].PosY_Fantasma - 1 >= 0:
                    if not self.detectar_colision_pared(self.fantasmas[i].PosX_Fantasma, self.fantasmas[i].PosY_Fantasma - 1):
                        self.fantasmas[i].PosY_Fantasma -= 1
                i+=1
                time.sleep(0.1)

    # metodo para detectar las teclas en la consola
    def teclas(self, tecla):
        if tecla.char == 'd':
            if not self.detectar_colision_pared(self.pacman.PosX + 1, self.pacman.PosY) and not self.colision_pacman_y_fantasmas():
                self.pacman.mover_derecha()
            else:
                print("Hay pared")
        elif tecla.char == 'a':
            if not self.detectar_colision_pared(self.pacman.PosX-1, self.pacman.PosY) and not self.colision_pacman_y_fantasmas():
                self.pacman.mover_izquierda()
            else:
                print("Hay pared")
        elif tecla.char == 'w':
            if not self.detectar_colision_pared(self.pacman.PosX, self.pacman.PosY - 1) and not self.colision_pacman_y_fantasmas():
                self.pacman.mover_arriba()
            else:
                print("Hay pared")
        elif tecla.char == 's':
            if not self.detectar_colision_pared(self.pacman.PosX, self.pacman.PosY + 1) and not self.colision_pacman_y_fantasmas():
                self.pacman.mover_abajo()
            else:
                print("Hay pared")
        elif tecla.char == 'k':
            self.imprimir_matriz()