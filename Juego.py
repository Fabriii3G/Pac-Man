#Modelo de objetos de la clase juego
import tkinter as tk
class Juego:
    #Atributos de la clase juego
    def __init__(self, Njuego, Tablero, Nivel, Score):
        self.Njuego = Njuego
        self.Tablero = Tablero
        self.Nivel = Nivel
        self.Score = Score
    #Metodos de la clase juego
    def iniciar_juego(self):
        self.ventanaJuego = tk.Toplevel()
        self.ventanaJuego.minsize(1000, 600)
        self.ventanaJuego.maxsize(1000, 600)
        self.ventanaJuego.title("Pac-Man")
        self.ventanaJuego.mainloop()
    def inicio(self):  # creacion de la ventana principal
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
        boton = tk.Button(self.window, image=jugar, bg="black", command=self.Ejecute_juego)
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

    def Ejecute_juego(self):
        self.window.withdraw()
        self.iniciar_juego()
    def jugar(self):  # creacion de la ventana jugar
        self.window.withdraw()
        self.jugar = tk.Tk()
        self.jugar.minsize(1000, 600)
        self.jugar.maxsize(1000, 600)
        self.jugar.title("jugar")
        self.jugar.configure(bg="black")
        self.jugar.mainloop()

    def salon_de_la_fama(self):  # creacion de la ventana Salon de la fama
        self.window.withdraw()
        self.salon = tk.Tk()
        self.salon.minsize(1000, 600)
        self.salon.maxsize(1000, 600)
        self.salon.title("Salon de la Fama")
        self.salon.configure(bg="black")
        self.salon.mainloop()

    def acerca_de(self):  # creacion de la ventana Acerca De
        self.window.withdraw()
        self.acerca = tk.Tk()
        self.acerca.minsize(900, 500)
        self.acerca.maxsize(900, 500)
        self.acerca.title("Acerca De")
        self.acerca.configure(bg="black")
        canva = tk.Canvas(self.acerca, width=900, height=500, bg="black")
        foto = tk.PhotoImage(master=canva, file="acerca.png")
        canva.create_image(450, 250, image=foto)
        canva.pack()
        canva.place(x=0, y=0)
        botonSalir = tk.Button(self.acerca, height=1, width=5, text="Salir", command=salir)
        botonSalir.place(x=428, y=465)
        self.acerca.mainloop()

    def ayuda(self):  # creacion de la ventana Ayuda
        self.window.withdraw()
        self.ayuda = tk.Toplevel()
        self.ayuda.minsize(1000, 600)
        self.ayuda.maxsize(1000, 600)
        self.ayuda.title("self.ayuda")
        self.ayuda.configure(bg="black")
        self.ayuda.mainloop()
