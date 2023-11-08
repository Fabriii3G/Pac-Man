import sys
import tkinter as tk
import pygame
import tkinter.messagebox
#Modelo de objetos de la clase juego
class Juego:
    #Atributos de la clase juego
    def __init__(self, Njuego, Tablero, Nivel, Score, pacman):
        self.Njuego = Njuego
        self.Tablero = Tablero
        self.Nivel = Nivel
        self.Score = Score
        self.pacman = pacman

    #Metodos de la clase juego
    def inicio(self):  # metodo de la ventana principal
        self.window = tk.Tk()
        self.window.minsize(1000, 600)
        self.window.maxsize(1000, 600)
        self.window.title("Pacman")
        self.window.configure(bg="black")
        canva = tk.Canvas(self.window, width=1000, height=600, bg="black")
        foto = tk.PhotoImage(master=canva, file="Fondo.png")
        canva.create_image(500, 299, image=foto)
        canva.pack()
        canva.place(x=0, y=0)
        # Boton Jugar
        jugar = tk.PhotoImage(file="Jugar.png")
        boton = tk.Button(self.window, image=jugar, bg="black", command=self.iniciar_juego)
        boton.pack()
        boton.place(x=440, y=290)
        # Boton Salon de la Fama
        salon = tk.PhotoImage(file="puntajes.png")
        boton = tk.Button(self.window, image=salon, bg="black", command=self.salon_de_la_fama)
        boton.pack()
        boton.place(x=440, y=400)
        # Boton Acerca De
        acerca = tk.PhotoImage(file="Info.png")
        boton = tk.Button(self.window, image=acerca, bg="black", command=self.acerca_de)
        boton.pack()
        boton.place(x=240, y=350)
        # Boton Ayuda
        ayuda = tk.PhotoImage(file="ayuda.png")
        boton = tk.Button(self.window, image=ayuda, bg="black", command=self.ayuda)
        boton.pack()
        boton.place(x=640, y=350)
        self.window.mainloop()

    def iniciar_juego(self): # metodo de la ventana de juego
        self.window.withdraw()

        pygame.init()
        self.pantalla = pygame.display.set_mode((1200, 780))
        pygame.display.set_caption("Pac-Man")
        fuente = pygame.font.Font("Minecraftia-Regular.ttf", 15)
        label = fuente.render("Puntaje: 0", True, (255, 255, 255))
        label_rect = label.get_rect()
        label_rect.topright = (1010, 10)
        pausa = True
        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_ESCAPE:
                        pausa = not pausa
                    elif evento.key == pygame.K_d:
                        if not self.Tablero.detectar_colision_pared(self.pacman.PosX + 1, self.pacman.PosY) and not self.Tablero.colision_pacman_y_fantasmas():
                            self.pacman.mover_derecha()
                            self.Tablero.puntaje()
                    elif evento.key == pygame.K_a:
                        if not self.Tablero.detectar_colision_pared(self.pacman.PosX - 1, self.pacman.PosY) and not self.Tablero.colision_pacman_y_fantasmas():
                            self.pacman.mover_izquierda()
                            self.Tablero.puntaje()
                    elif evento.key == pygame.K_w:
                        if not self.Tablero.detectar_colision_pared(self.pacman.PosX, self.pacman.PosY - 1) and not self.Tablero.colision_pacman_y_fantasmas():
                            self.pacman.mover_arriba()
                            self.Tablero.puntaje()
                    elif evento.key == pygame.K_s:
                        if not self.Tablero.detectar_colision_pared(self.pacman.PosX, self.pacman.PosY + 1) and not self.Tablero.colision_pacman_y_fantasmas():
                            self.pacman.mover_abajo()
                            self.Tablero.puntaje()
                    elif evento.key == pygame.K_k:
                        self.imprimir_matriz()
            if pausa:
                self.pantalla.fill((0, 0, 0))
                self.dibujar_matriz()
                self.Tablero.actualizar_matriz()
                label = fuente.render(f"Puntaje: {self.Tablero.puntos}", True, (255, 255, 255))
                self.pantalla.blit(label, label_rect)
                pygame.display.update()
                reloj = pygame.time.Clock()
                reloj.tick(60)


    def dibujar_matriz(self):
        pacman_imagen = pygame.image.load("pacman.png")
        fantasmaR_imagen = pygame.image.load("rojo.png")
        fantasmaN_imagen = pygame.image.load("naranja (1).png")
        fantasmaC_imagen = pygame.image.load("celeste (1).png")
        fantasmar_imagen = pygame.image.load("rosado (1).png")
        cereza_imagen = pygame.image.load("cereza (1).png")
        punto_imagen = pygame.image.load("punto.png")
        capsula_imagen = pygame.image.load("capsula (1).png")
        pared_imagen = pygame.image.load("muro (1).png")
        for fila in range(len(self.Tablero.matriz)):
            for columna in range(len(self.Tablero.matriz[0])):
                if self.Tablero.matriz[fila][columna] == 0:
                    self.pantalla.blit(pared_imagen,(columna * 30, fila * 30))
                elif self.Tablero.matriz[fila][columna] == '🟡':
                    self.pantalla.blit(pacman_imagen, (columna * 30, fila * 30))
                elif self.Tablero.matriz[fila][columna] == 1 :
                    self.pantalla.blit(punto_imagen, (columna * 30, fila * 30))
                elif self.Tablero.matriz[fila][columna] == 'R' :
                    self.pantalla.blit(fantasmaR_imagen, (columna * 30, fila * 30))
                elif self.Tablero.matriz[fila][columna] == 'N' :
                    self.pantalla.blit(fantasmaN_imagen, (columna * 30, fila * 30))
                elif self.Tablero.matriz[fila][columna] == 'C':
                    self.pantalla.blit(fantasmaC_imagen, (columna * 30, fila * 30))
                elif self.Tablero.matriz[fila][columna] == 'r' :
                    self.pantalla.blit(fantasmar_imagen, (columna * 30, fila * 30))
                elif self.Tablero.matriz[fila][columna] == 3 :
                    self.pantalla.blit(cereza_imagen, (columna * 30, fila * 30))
                elif self.Tablero.matriz[fila][columna] == 2 :
                    self.pantalla.blit(capsula_imagen, (columna * 30, fila * 30))

    def salon_de_la_fama(self):  # metodo de la ventana Salon de la fama
        self.window.withdraw()
        self.salon = tk.Toplevel()
        self.salon.minsize(1000, 600)
        self.salon.maxsize(1000, 600)
        self.salon.title("Salon de la Fama")
        self.salon.configure(bg="black")
        botonSalir = tk.Button(self.salon, height=1, width=5, text="Salir", command=self.salir_salon)
        botonSalir.place(x=428, y=465)
        self.salon.mainloop()

    def acerca_de(self):  # metodo de la ventana Acerca De
        self.window.withdraw()
        self.acerca = tk.Toplevel()
        self.acerca.minsize(900, 500)
        self.acerca.maxsize(900, 500)
        self.acerca.title("Acerca De")
        self.acerca.configure(bg="black")
        canva = tk.Canvas(self.acerca, width=900, height=500, bg="black")
        foto = tk.PhotoImage(master=canva, file="acerca.png")
        canva.create_image(450, 250, image=foto)
        canva.pack()
        canva.place(x=0, y=0)
        botonSalir = tk.Button(self.acerca, height=1, width=5, text="Salir", command=self.salir_acerca)
        botonSalir.place(x=428, y=465)
        self.acerca.mainloop()

    def ayuda(self):  # metodo de la ventana Ayuda
        self.window.withdraw()
        self.ayuda = tk.Toplevel()
        self.ayuda.minsize(1000, 600)
        self.ayuda.maxsize(1000, 600)
        self.ayuda.title("self.ayuda")
        self.ayuda.configure(bg="black")
        botonSalir = tk.Button(self.ayuda, height=1, width=5, text="Salir", command=self.salir_ayuda)
        botonSalir.place(x=428, y=465)
        self.ayuda.mainloop()

    def salir_juego(self): # metodo de retornar a ventana principal
        self.ventanaJuego.withdraw()
        self.window.deiconify()

    def salir_salon(self): # metodo de retornar a ventana principal
        self.salon.withdraw()
        self.window.deiconify()

    def salir_acerca(self): # metodo de retornar a ventana principal
        self.acerca.withdraw()
        self.window.deiconify()

    def salir_ayuda(self): # metodo de retornar a ventana principal
        self.ayuda.withdraw()
        self.window.deiconify()



