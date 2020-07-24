from tkinter import *
import pygame
import os

# Defining MusicPlayer Class
class ReproductorMusical:
    
    def __init__(self,container):
        self.container = container
        # Titulo de la ventana
        self.container.title("Music Player")
        # Tamaño
        self.container.geometry("1000x600")
         # Bloquear le cambio de tamaño
        self.container.resizable(width=False, height=False)
        # Iniciar Pygame
        pygame.init()
        # Iniciar Pygame Mixer
        pygame.mixer.init()
        
        self.estado = StringVar()
        self.cancion = StringVar()
        
        
# Creating TK Container
container = Tk()
# Passing Root to MusicPlayer Class
ReproductorMusical(container)
# Root Window Looping
container.mainloop()
