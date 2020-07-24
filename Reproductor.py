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

        # Frame para el titulo de la cancion
        contenedorCancion = LabelFrame(self.container,text="Título",font=("fonatica",10,"bold"),bg="grey",fg="white",bd=5,relief=FLAT)
        contenedorCancion.place(x=0,y=500,width=600,height=100)
        # Se inserta mensaje del estado en el label del titulo de la cancion
        titulo = Label(contenedorCancion,textvariable=self.cancion,width=30,font=("fonatica",15,"bold"),bg="grey",fg="white").grid(row=0,column=0,padx=10,pady=5)
        # Etiqueta para identificar el estado de ejecucion de la cancion
        estadoCancion = Label(contenedorCancion,textvariable=self.estado,font=("fonatica",15,"bold"),bg="grey",fg="white").grid(row=0,column=1,padx=10,pady=5)

        # Contenedor de botones
        contenedorBotones = LabelFrame(self.container,text="Control Panel",font=("fonatica",15,"bold"),bg="grey",fg="white",bd=5,relief=FLAT)
        contenedorBotones.place(x=600,y=500,width=400,height=100)
        # Boton de play
        playBtn = Button(contenedorBotones,text=">",command=self.ReproducirCancion,width=6,height=1,font=("fonatica",12),fg="black",bg="grey").grid(row=0,column=0,padx=10,pady=5)
        # Boton de Pause
        pausaOnBtn = Button(contenedorBotones,text="||",command=self.pausarCancion,width=8,height=1,font=("fonatica",12),fg="black",bg="grey").grid(row=0,column=1,padx=10,pady=5)
        # Boton de Stop
        stopBtn = Button(contenedorBotones,text="[]",command=self.detenerCancion,width=6,height=1,font=("fonatica",12),fg="black",bg="grey").grid(row=0,column=2,padx=10,pady=5)
        
        # PLaylist
        contenedorCanciones = LabelFrame(self.container,text="Playlist",font=("fonatica",15,"bold"),bg="black",fg="white",bd=5,relief=FLAT)
        contenedorCanciones.place(x=0,y=0,width=1000,height=500)
        # Scrollbar de la playlist
        scrol_y = Scrollbar(contenedorCanciones,orient=VERTICAL)
        # Insertando listbox de la Playlist
        self.playlist = Listbox(contenedorCanciones,yscrollcommand=scrol_y.set,selectbackground="black",selectmode=SINGLE,font=("fonatica",12,"bold"),bg="silver",fg="navyblue",bd=5,relief=GROOVE)
        # Applying Scrollbar to listbox
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.playlist.yview)
        self.playlist.pack(fill=BOTH)
        # Seleccionando directorio de las canciones
        os.chdir(r'C:\Users\alejo\Music')
        # Obteniendo canciones
        songtracks = os.listdir()
        # Insertando canciones en el playlist
        for track in songtracks:
            self.playlist.insert(END,track)
        
    # Definiendo las funciones para la ejecucion de las canciones
    def ReproducirCancion(self):
        # Mostrando el titulo de la canción
        self.cancion.set(self.playlist.get(ACTIVE))
        print(self.estado.get())
        if self.estado.get() == "-Paused":
            self.desPausar()
        else:    
            # Mostrando el estado de la ejecucion
            self.estado.set("-Playing")
            # Cargando la cancion seleccionada
            pygame.mixer.music.load(self.playlist.get(ACTIVE))
            # Ejecutando la cancion seleccionada
            pygame.mixer.music.play()
    
    def pausarCancion(self):
        # Mostrando el estado de la ejecucion
        self.estado.set("-Paused")
        # Pausando la cancion
        pygame.mixer.music.pause()
    
    def detenerCancion(self):
        # Mostrando el estado de la ejecucion
        self.estado.set("-Stopped")
        # Deteniendo cancion
        pygame.mixer.music.stop()
    
    def desPausar(self):
        # Mostrando el estado de la ejecucion
        self.estado.set("-Playing")
        # Ejecutando cancion despues de pausada
        pygame.mixer.music.unpause()

       
        
# Creating TK Container
container = Tk()
# Passing container to MusicPlayer Class
ReproductorMusical(container)
# container Window Looping
container.mainloop()
