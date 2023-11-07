import random
import time
import threading

# funcionamiento de la matriz:
# 0: Pared
# 1: Alimento/Puntos

# tareas 6 noviembre
# crear metodos de que pacman pueda comerse a los fantasmas
# tratar de empezar a graficar el juego
# entender bien el funcionamiento de los diferentes tipos de alimentos

class Matriz:
    def __init__(self, matriz, Pacman, Fantasmas):
        self.matriz = matriz
        self.pacman = Pacman
        self.fantasmas = Fantasmas
        self.puntos = 0
        self.posicionesPacman= [self.pacman.PosX, self.pacman.PosY]
        #self.posicionesFantama = [self.fantasma.PosX_Fantasma, self.fantasma.PosY_Fantasma]

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
        self.matriz[self.fantasmas[0].PosY_Fantasma][self.fantasmas[0].PosX_Fantasma] = "R"
        self.matriz[self.fantasmas[1].PosY_Fantasma][self.fantasmas[1].PosX_Fantasma] = "C"
        self.matriz[self.fantasmas[2].PosY_Fantasma][self.fantasmas[2].PosX_Fantasma] = "N"
        self.matriz[self.fantasmas[3].PosY_Fantasma][self.fantasmas[3].PosX_Fantasma] = "r"


    # metodo que imprime la matriz
    def imprimir_matriz(self):
        self.actualizar_matriz()
        for fila in self.matriz:
            for elemento in fila:
                print(elemento, end="\t")
            print()
        print(f"PosicionX_Pacman:{self.pacman.PosX}, PosicionY_Pacman: {self.pacman.PosY}")
        print(f"Puntos: {self.puntos}")
        #print(f"PosicionX_fantasma:{self.fantasma.PosX_Fantasma}, PosicionY_fantasma: {self.fantasma.PosY_Fantasma}")

        print("-------------------------------")

    # metodo de puntaje
    def puntaje(self):
        if self.matriz[self.pacman.PosY][self.pacman.PosX] == 1:
            self.puntos += 5
            self.matriz[self.pacman.PosY][self.pacman.PosX] = 4 # Elimina el punto de la celda


    # metodo que detecta si hay pared antes de hacer el movimiento
    def detectar_colision_pared(self, x, y):
        return self.matriz[y][x] == 0 #Retorna el valor booleano si la posicion ingresada es una pared

    # metodo que detecta la colision entre pacman y los fantasmas
    def colision_pacman_y_fantasmas(self):
        i = 0
        while i<len(self.fantasmas):
            if self.pacman.PosX == self.fantasmas[i].PosX_Fantasma and self.pacman.PosY == self.fantasmas[i].PosY_Fantasma:
                self.matriz[self.posicionesPacman[1]][self.posicionesPacman[0]] = 1
                self.pacman.set_estado("Muerto")
                print("Pacman ha muerto")
                return True
            i +=1

        # metodo para hilo que se encarga del movimiento de los fantasmas
    def hilo(self):
        hilo = threading.Thread(target=self.mover_fantasma)
        hilo.daemon = True
        hilo.start()

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
                        self.colision_pacman_y_fantasmas()
                elif direccion == 'Izquierda' and self.fantasmas[i].PosX_Fantasma - 1 >= 0:
                    if not self.detectar_colision_pared(self.fantasmas[i].PosX_Fantasma - 1, self.fantasmas[i].PosY_Fantasma):
                        self.fantasmas[i].PosX_Fantasma -= 1
                        self.colision_pacman_y_fantasmas()
                elif direccion == 'Abajo' and self.fantasmas[i].PosY_Fantasma + 1 < filas:
                    if not self.detectar_colision_pared(self.fantasmas[i].PosX_Fantasma, self.fantasmas[i].PosY_Fantasma + 1):
                        self.fantasmas[i].PosY_Fantasma += 1
                        self.colision_pacman_y_fantasmas()
                elif direccion == 'Arriba' and self.fantasmas[i].PosY_Fantasma - 1 >= 0:
                    if not self.detectar_colision_pared(self.fantasmas[i].PosX_Fantasma, self.fantasmas[i].PosY_Fantasma - 1):
                        self.fantasmas[i].PosY_Fantasma -= 1
                        self.colision_pacman_y_fantasmas()
                i+=1
                time.sleep(0.1)

    # metodo para detectar las teclas en la consola
    def teclas(self, tecla):
        if tecla.char == 'd':
            if not self.detectar_colision_pared(self.pacman.PosX + 1, self.pacman.PosY) and not self.colision_pacman_y_fantasmas():
                self.pacman.mover_derecha()
                self.puntaje()
            else:
                print("Hay pared")
        elif tecla.char == 'a':
            if not self.detectar_colision_pared(self.pacman.PosX-1, self.pacman.PosY) and not self.colision_pacman_y_fantasmas():
                self.pacman.mover_izquierda()
                self.puntaje()
            else:
                print("Hay pared")
        elif tecla.char == 'w':
            if not self.detectar_colision_pared(self.pacman.PosX, self.pacman.PosY - 1) and not self.colision_pacman_y_fantasmas():
                self.pacman.mover_arriba()
                self.puntaje()
            else:
                print("Hay pared")
        elif tecla.char == 's':
            if not self.detectar_colision_pared(self.pacman.PosX, self.pacman.PosY + 1) and not self.colision_pacman_y_fantasmas():
                self.pacman.mover_abajo()
                self.puntaje()
            else:
                print("Hay pared")
        elif tecla.char == 'k':
            self.imprimir_matriz()